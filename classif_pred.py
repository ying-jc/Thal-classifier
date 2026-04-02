#!/usr/bin/env python

import pandas as pd
import os
from autogluon.tabular import TabularPredictor

def mod_prediction(infile,conf,cutoff,terminal,out):
    mod_path = ex_config(conf)
    sample_na, exp_mat = ex_exp(infile)
    df = pd.DataFrame(exp_mat,columns=['RDWSD','RBC','MCV','HCT','MCHC','MCH','RDWCV','HGB'])
    mypath = os.getcwd()
    os.chdir(mypath)    
    clf = TabularPredictor.load(path=mod_path)
    pp = clf.predict_proba(data=df, model='WeightedEnsemble_L2Best')[1]
    pred = clf.predict(data=df, model='WeightedEnsemble_L2Best', decision_threshold=cutoff)
    df_prob = pd.DataFrame(pp.tolist(),columns=['Probability of thalassemia'],index=sample_na)
    df_prob['Prediction of thalassemia'] = pred.tolist()
    if terminal == 'True':
        print('\n'.join(['Result of prediction:']))
        print(df_prob)    
    if out != None:
        df_prob.to_csv(mypath+'/'+out,sep='\t')
        print('\nThe result of prediction has been saved to '+out+'!')        
    
def ex_config(cf):
    cfs = open(cf).read().strip().split('\n')
    cfs = [z for z in cfs if not z.startswith('#')]
    mod_path = cfs[0].split('=')[-1].strip()
    return mod_path

def ex_exp(mat):
    mats = open(mat).read().strip().split('\n')
    gexps = [[float(c) for c in b.split('\t')[1:]] for b in mats if not b.startswith('#')]
    nsamp = [b.split('\t')[0] for b in mats if not b.startswith('#')]
    return nsamp, gexps
    