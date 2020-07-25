# Internship Project MyT

This project is about identifying HIV indicators in Dutch clinical narrative data by using the string matching tools QuickUMLS and Regular Expresions in Python. 
The Jupyter notebook 'QuickUMLS Dut Eng and RegEx and Eval Scores' and the py-file 'Creating_rex_ex_list' can be downloaded. Note, before opening the notebook in the terminal type in: ulimit -n 4096. After that open the notebook. Otherwise, the notebook will be temporarily unavailable. 

imports are:

from pathlib import Path

from quickumls import QuickUMLS

import os

import re

from collections import defaultdict

import pandas as pd

The last cell of the notebook contains the variables with paths to the files. Below I explain the variables:

1. qumls_file: path to files where the Dutch UMLS files are stored;
2. qumls_file_eng: path to files where the English UMLS files are stored;
3. path_to_directory: path to directory where the clinical notes are stored. Clinical notes should be .txt extension; 
4. condition_file: path to file where the HIV indicators are stored. This file should be in xls or csv extention. Each separate indicator should be on a separate row in the first column;
5. path_to_manual_annotations: path to file where the manual annotations are stored. This file should be in xls or csv extension. 
    The file should have two columns. 
    The first column should get the name of the clincal note in the format: Notex.doc (here x is the number of the note);
    The second column contains the HIV indicator. If an HIV indicator occurs multiple times in the same note, the row should be duplicated, e.g.:
      1. Note4.doc	longontsteking
      2. Note4.doc	longontsteking
 Due to privacy regulations I cannot provide the above files. 
 
 The key argument 'combined' in the function create_xls_file means which versions of UMLS should be used:
 Default is "yes" which means that English, Dutch versions of UMLS and regular expressions are used;
 "nlen" means that English, Dutch versions of UMLS are used without regular expressions;
 "nl" means that only the Dutch version of UMLS is used;
 "en" means that only the English version of UMLS is used.
 
 This can be used for comparing the evaluations scores of the versions of UMLS with or without regular expressions. 
 
 The function creating_reg_ex_list  in the file 'Creating_rex_ex_list' creates a list of the HIV indicators which are not recognized by both the Dutch and English version and searches for these terms in the notes. 
 
 After executing the notebook it should return recall, precision and f-scores of the identified HIV indicators by the Dutch and English version of QuickUMLS and regular expressions in the clinical notes tested against the manual annotated notes. 
    

