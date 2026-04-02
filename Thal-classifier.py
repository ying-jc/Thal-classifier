#!/usr/bin/env python

import classif_pred
import click

@click.command()
@click.option('--conf', nargs=1, required=False, type=str, prompt='Config file name', help='Configuration file in plain text format. (Required)')
@click.option('--infile', nargs=1, required=False, type=str, prompt='CBC file name', help='CBC data file in tab-delimited text format. (Required)')
@click.option("--cutoff", nargs=1, required=False, default=0.439,type=click.FloatRange(0,1), help="Cutoff value for binary classification. [Default: 0.439] (Optional)")
@click.option('--terminal', nargs=1, required=False, default='True', type=click.Choice(['True', 'False'], case_sensitive=True), help='Output result to the terminal. [Default: True] (Optional)')
@click.option('--out', nargs=1, required=False, default=None, type=str, help='The name of the output file in tab-delimited text format. (Optional)')

def run_command(infile,conf,cutoff,terminal,out):
    """Thal-classifier: an interpretable ensemble learning model for thalassemia detection in pregnant women using routine hematological parameters"""
    classif_pred.mod_prediction(infile,conf,cutoff,terminal,out)
    print('\nWork done!')

if __name__ == '__main__':
    run_command()
    