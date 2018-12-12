"""
This python file is used to query useful data from datasets,
then store or generate a new csv file
in the workflow, after user input something, code will go into this
module and fetch data they need.
"""
import pandas as pd

def query(data, list_groupby, list_tolist, join_column):
    """
    basic query function that query from large datasets
    input data is database we will query from, list_groupby is the column
    we need to groupby, the list_tolist is merge this column Information
    if they group to one row, and join_column is what column we merge into,
    group by a list of column and make a list of column to a list
    and generate and return a panda dataframe
    """
    list_all = []
    for item in list_tolist:
        df_tem = data.groupby(list_groupby)[item].apply(lambda x: x.tolist())
        df_tem = df_tem.reset_index()
        list_all.append(df_tem)

    count = 0
    for item in list_all:
        if count == 0:
            count = count + 1
            continue
        else:
            list_all[0] = pd.merge(item, list_all[0], how='inner', left_on=join_column,
                                   right_on=join_column)

    return list_all[0]

def query_single(data, column_name, column_value, list_groupby, list_tolist, join_column):
    """
    input data is database we will query from. column_name and column_value
    is your condition to get specific row. List_groupby is the column
    we need to groupby. The list_tolist is merge this column Information
    if they group to one row, and join_column is what column we merge into.
    after query, we get a groupby data set
    and this function only get one specific row dataframe to return
    """
    df_all = query(data, list_groupby, list_tolist, join_column)
    return df_all.loc[df_all[column_name] == column_value]

def filter_query(df_all, column_name, column_value, signal):
    """
    df_all is dataframe we need to query from,  column_name, column_value, signal
    are condition we use to filter information
    This function is used to filter the data that output from "query" function.
    after query, you could use it to generate several line of data base on
    your condition. Return a multiple row dataframe
    """
    if signal == '=':
        data = df_all.loc[df_all[column_name] == column_value]
    elif signal == '<':
        data = df_all.loc[df_all[column_name] < column_value]
    elif signal == '>':
        data = df_all.loc[df_all[column_name] > column_value]
    else:
        print('signal not find')
        return None
    return data

def narms_query(file_name, data_year, age_group, output_filename='narms_out.csv'):
    """
    file_name is input dataset and  data_year, age_group is filter Condition.
    output_filename='narms_out.csv' is your output file name
    Function narms_query is used to query data from "narms processed.csv"
    we will generate the dataset by input year and age Condition
    we will return a one row dataset for query.
    """
    df_all = pd.read_csv(file_name)
    df_all = df_all.loc[df_all['Data_Year'] == data_year]
    df_all = df_all.loc[df_all['Age_Group'] == age_group]
    df_all.to_csv(output_filename, index=False)
    return df_all

if __name__ == '__main__':
    DF_ALL = narms_query("narm's processed.csv", 1996, '0-4')
