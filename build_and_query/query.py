import pandas as pd

def query(list_groupby, list_tolist, join_column):
    list_all = []
    for item in list_tolist:
        df_tem = df.groupby(list_groupby)[item].apply(lambda x : x.tolist())
        list_all.append(df_tem)
        print(df_tem)

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
    print("Successfully")
    return list_all[0]

if __name__ == '__main__':
    df=pd.read_csv('test_file.csv')
    #df = pd.DataFrame(data=d)
    output=query(["subject_id","hadm_id"],["drug_type","drug","drug_name_poe","drug_name_generic","formulary_drug_cd"],["subject_id","hadm_id"])
    output.to_csv('test_out.csv')
    outputs=pd.read_csv('test_out.csv')