""" This python file is used to query useful data from datasets,
then store or generate a new csv file
"""
import pandas as pd

def query(data, list_groupby, list_tolist, join_column):
    """
    group by a list of column and make a list of column to a list
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
    group by a list of column and make a list of column to a list
    and only get one specific row
    """
    df_all = query(data, list_groupby, list_tolist, join_column)
    #print(df_all)
    return df_all.loc[df_all[column_name] == column_value]

def filter_query(df_all, column_name, column_value, signal):
    """
    This function is used to filter the data that output from "query" function.
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
    Function narms_query is used to query data from "narms processed.csv"
    """
    df_all = pd.read_csv(file_name)
    df_all = df_all.loc[df_all['Data_Year'] == data_year]
    df_all = df_all.loc[df_all['Age_Group'] == age_group]
    df_all.to_csv(output_filename, index=False)
    return df_all

if __name__ == '__main__':
    DF_ALL = narms_query("narm's processed.csv", 1996, '0-4')
