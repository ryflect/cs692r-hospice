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

# Reference function 3
# get_scatter_marker_size(col_array, min_size, max_size)
#
# Purpose: Returns a resized scatter marker array given an array of data, scaled in the range [min_size, max_size]
# 
# Input: col_array: an array of data points
#        min_size: desired area of the smallest point
#        max_size: desired area of the largest point
#
# Returns: Array of marker sizes to be passed as the 's' argument to plt.scatter()

def get_scatter_marker_size(col_array, min_size=10, max_size=1000):
    c_min = np.min(col_array)
    c_max = np.max(col_array)
    return [((i - c_min) * (max_size - min_size) / (c_max - c_min)) + min_size for i in col_array]

# get the co-effs of best fit for first and second order poly for a heatmap
# Reference function 4
# get_coeffs(dframe, n)
#
# Purpose: Returns the co-effs of best fit for first and second order poly for a heatmap data frame having n hos_weeks (or similar time unit along x)
# 
# Input: dframe: a data frame of the heatmap data
#        n: no. of hos_week (or similar time unit along x)
#
# Returns: Data frame appended to heatmap data with co-effs (m, x2, x1)
def get_coeffs(df_hm, n):
    # correct way
    dft = df_hm.apply(lambda x: np.polyfit(y=x, x=np.linspace(0, n, n+1), deg=1) if np.sum(np.isfinite(x)) == n+1 else 'undef', axis=1)
    dft = dft.to_frame().rename(columns={0: 'deg1 (m)'})
    dft['deg1 (m)'] = dft['deg1 (m)'].apply(lambda x: x if isinstance(x, str) else np.round(x[0], 2))
    dft_2 = df_hm.apply(lambda x: np.polyfit(y=x, x=np.linspace(0, n, n+1) , deg=2) if np.sum(np.isfinite(x)) == n+1 else 'undef', axis=1).to_frame().rename(columns={0: 'deg2'})
    dft_2 = dft_2['deg2'].apply(lambda x: ['undef', 'undef'] if isinstance(x, str) else x[0:2])
    dft_2 = pd.DataFrame(dft_2.to_list(), columns=['deg2 (x2)', 'deg2 (x1)'], index=dft_2.index)
    dft = pd.concat([dft, dft_2], axis=1)
    dft['deg2 (x2)'] = dft['deg2 (x2)'].apply(lambda x: np.round(x, 2) if isinstance(x, float) else x)
    dft['deg2 (x1)'] = dft['deg2 (x1)'].apply(lambda x: np.round(x, 2) if isinstance(x, float) else x)
    return pd.concat([df_hm, dft], axis=1)  
