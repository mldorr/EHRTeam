import pandas as pd

def query(df, list_groupby, list_tolist, join_column):
    list_all = []
    for item in list_tolist:
        df_tem = df.groupby(list_groupby)[item].apply(lambda x : x.tolist())
        list_all.append(df_tem)
        #print(df_tem)

    count = 0
    while count < len(list_all):
        list_all[count] = list_all[count].to_frame()
        count = count + 1


    count = 0
    for item in list_all:
        if count == 0:
            count = count + 1
            continue
        else:
            list_all[0] = pd.merge(item, list_all[0], how='inner',left_on=join_column, right_on=join_column)

    print("Successful")
    return list_all[0]

def querySingle(df, column_name, column_value, list_groupby, list_tolist, join_column):
    df_all = query(df, list_groupby, list_tolist, join_column)
    df_all.reset_index(inplace=True)
    #print(df_all)
    return df_all.loc[df_all[column_name] == column_value]

def filter(df_all, column_name, column_value, signal):
    df_all.reset_index(inplace=True)
    if (signal == '='):
        return df_all.loc[df_all[column_name] == column_value]
    elif (signal == '<'):
        return df_all.loc[df_all[column_name] < column_value]
    elif (signal == '>'):
        return df_all.loc[df_all[column_name] == column_value]
    else :
        print('signal not find')

def narms_query(file_name, data_year, age_group,output_filename = 'narms_out.csv'):
    df_all = pd.read_csv(file_name)
    df_all = df_all.loc[df_all['Data_Year'] == data_year]
    df_all = df_all.loc[df_all['Age_Group'] == age_group]
    for column in list(df_all.columns.values):
        #print(column)
        #print(df_all.iloc[0, df_all.columns.get_loc(column)])
        if(df_all.iloc[0, df_all.columns.get_loc(column)] == 0):
            df_all = df_all.drop(columns = column)
    print(list(df_all.columns.values))
    df_all.to_csv(output_filename,index = False)
    print('successful')

if __name__ == '__main__':
    #narms_query("narm's processed.csv", 1996, '0-4')

    df=pd.read_csv('test_file.csv')
    #df = pd.DataFrame(data=d)
    subject_ids = int(input('Enter subject_id (e.g., 61): '))

    output=query(df,["subject_id","hadm_id"], ["drug_type","drug","drug_name_poe",
    "drug_name_generic","formulary_drug_cd"], ["subject_id","hadm_id"])
    output = filter(output, 'subject_id', 66, '<'  )
    print(output)
    output.to_csv('test_out.csv',index = False)
    outputs=pd.read_csv('test_out.csv')
