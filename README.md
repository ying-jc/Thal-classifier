# Thal-classifier
A clinically applicable and interpretable machine learning model for thalassemia detecting in pregnant women

## Installation  
Clone Thal-classifier by  
```
$ git clone https://github.com/ying-jc/Thal-classifier.git
```  
or
Download Thal-classifier (ZIP file), move it to a directory where the user wants it installed, and uncompress it.

## Requirements  
Thal-classifier is an open-source Python-based tool, which operates depending on the Python environment. Currently, Thal-classifier has only been tested on the Windows 10 system with Python version 3.12.11. Before running Thal-classifier, the user should make sure all the following packages are installed in their Python environment: click, pandas, and autogluon. These packages can be easily installed using pip by
```
$ pip install -r requirements.txt
```

## Usage  
### Options  
For details of all options, run:  
```
$ python Thal-classifier.py --help

Usage: Thal-classifier.py [OPTIONS]

  Thal-classifier: an interpretable ensemble learning model for thalassemia
  detection in pregnant women using routine hematological parameters

Options:
  --conf TEXT              Configuration file in plain text format. (Required)

  --infile TEXT            Gene expression file in tab-delimited text format.
                           (Required)

  --cutoff FLOAT RANGE     Cutoff value for binary classification. [Default:
                           0.439] (Optional)  [0<=x<=1]  

  --terminal [True|False]  Output result to the terminal. [Default: True]
                           (Optional)

  --out TEXT               The name of the output file in tab-delimited text
                           format. (Optional)

  --help                   Show this message and exit.
```  

### Notes  
#### Input
The input to Thal-classifier must be a tab-delimited file containing CBC data for any number of samples. Each sample is required to provide the values of 8 parameters. An example of the input file can be found in the directory of example.

#### Output
Thal-classifier outputs the results to the terminal by default. The user can specify the name of the output file to save the results to a tab-delimited file. In the results, the first column represents the sample name, the second column represents the estimated probability of thalassemia for the corresponding sample, and the third column represents the classification according to the provided cutoff value.

#### Configuration file
The configuration file must be specified to tell the Thal-classifier where the classifiers are located. A template of the configuration file can be found in the main directory of Thal-classifier.

## An example  
All files in the commands can be found in the directory of Thal-classifier.  
* Set up the configuration file.

* Locate to the example folder:
```
$ cd Thal-classifier/example
```
* Run the following command to predict the sequences in the example with the default settings:
```
$ python ../Thal-classifier.py --conf ../config.txt --infile example.tab
```
Note that if the user is not running the program under the Thal-classifier folder, the path to Thal-classifier and config.txt needs to be provided.

## Citation  
Wang Q, Dai X, Xu K, Xu M, Ying J. Development of an interpretable ensemble learning model for thalassemia detection in pregnant women using routine hematological parameters. Digit Health. 2025 Nov 13;11:20552076251396982.
