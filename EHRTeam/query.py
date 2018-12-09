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


    #count = 0
    #while count < len(list_all):
    #    list_all[count] = list_all[count].to_frame()
    #    count = count + 1

    count = 0
    for item in list_all:
        if count == 0:
            count = count + 1
            continue
        else:
            list_all[0] = pd.merge(item, list_all[0], how='inner', left_on=join_column,
                                   right_on=join_column)
    #print(list_all[0])
    #list_all[0] = list_all[0].reset_index()
    #list_all[0].to_csv('query_test.csv')
    #print("Successful")
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
    for column in list(df_all.columns.values):
        #print(column)
        #print(df_all.iloc[0, df_all.columns.get_loc(column)])
        if(df_all.iloc[0, df_all.columns.get_loc(column)] == 0):
            df_all = df_all.drop(columns=column)
    print(list(df_all.columns.values))
    df_all.to_csv(output_filename, index=False)
    print('successful')

if __name__ == '__main__':
    #narms_query("narm's processed.csv", 1996, '0-4')

    DF = pd.read_csv('test_file.csv')
    #df = pd.DataFrame(data=d)
    #subject_ids = int(input('Enter subject_id (e.g., 61): '))
    LIST_TOLIST = ['hadm_id', 'Code', 'Descriptor',	'icd9_code',
                   'long_title', 'admission_type',	'diagnosis', 'insurance', 'language', 'religion',
                   'marital_status', 'ethnicity', 'gender', 'expire_flag', 'age',	'age_death',
                   'age_group', 'admit_year', 'admit_new', 'disch_new', 'description',
                   'drug_type', 'drug', 'formulary_drug_cd']
    OUTPUT = query_single(DF, 'subject_id', 61, ["subject_id"], LIST_TOLIST, "subject_id")
    #output = filter(output, 'subject_id', 66, '<'  )
    print(OUTPUT)
    #output.to_csv('test_out.csv',index = False)
    #outputs=pd.read_csv('test_out.csv')
