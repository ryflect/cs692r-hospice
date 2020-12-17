# Contains all of the reference functions used in different notebooks 
# (prototyping of these functions present in Reference.ipynb)

# imports
import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 

# Reference function 1
# get_file_names(col_names, df_ref)
#
# Purpose: Returns the file names of all tables containing all of the columns specified in col_names using df_ref
# 
# Input: col_names: List containing desired column names
#        df_ref: Reference dframe (cross_ref_cols_tabs.csv)
#
# Returns: List of file names containing all of the col_names

def get_file_names(col_names, df_ref):
    file_names = []
    # get list of files where the col has at least 1 entry
    for col in col_names:
        file_names.append(df_ref.iloc[df_ref.loc[:, col].dropna().index,0].tolist())
    # get the intersection of file_names for all cols
    file_names = list(set.intersection(*map(set, file_names)))
    return file_names


# Reference function 2
# get_histplot(col_names, df_ref, labels)
#
# Purpose: Returns a histogram of value_counts of column specified in col_name present in df_ref using IDEHR as the counter
# 
# Input: col_name: Column name
#        df_ref: Data
#        label: Column label
#
# Returns: Histplot of the value_counts of the columns

def get_histplot(col_name, df_ref, label):
    print('No. of unique IDEHR: ', len(df_ref[['IDEHR', col_name]].dropna().IDEHR.unique()))
    plt.rcParams['figure.figsize'] = [15, 8]
    matplotlib.rcParams.update({'font.size': 15})
    plt.figure()
    fig, ax = plt.subplots()
    ax = sns.histplot(data=df_ref[['IDEHR', col_name]].dropna().IDEHR.value_counts())
    ax.set_title(label)
    ax.set_xlabel('No. of observations')
    ax.set_ylabel('No. of IDEHRs')
    plt.grid()
    plt.show()
