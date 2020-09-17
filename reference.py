# Contains all of the reference functions used in different notebooks 
# (prototyping of these functions present in Reference.ipynb)

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
