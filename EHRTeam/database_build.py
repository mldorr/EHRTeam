"""
database_build
used to import and merge dataframes
"""

#import os
import numpy as np
import pandas as pd

def salmonella_rctc_processor(salmonella_tc):
    """
    selects only ICD-9 salmonella trigger codes

    Input: salmonella_tc: The trigger code of salmonella
    Output: salmonella_icd: ICD-9 salmonella trigger codes

    """
    salmonella_icd = salmonella_tc[salmonella_tc.CodeSystem == 'ICD9CM']
    return salmonella_icd

def admissions_processor(admissions):
    """
    creates age_group variable and reprocesses dates from random
    future dates (how the EHR was anonymized) to match the MIMIC
    dataframe date range

    Input: admissions: The imported "minic_admissions.csv"
    Output: admissions: "minic_admissions.csv" with "age_group" processed
            admissions2: "minic_admissions.csv" with "year" precessed
    """
    admissions['age_group'] = pd.Series(np.zeros(admissions.shape[0]))
    admissions.loc[(admissions['age'] > 0) &
                   (admissions['age'] < 5), 'age_group'] = '0-4'
    admissions.loc[(admissions['age'] >= 5) &
                   (admissions['age'] < 10), 'age_group'] = '5-9'
    admissions.loc[(admissions['age'] >= 10) &
                   (admissions['age'] < 20), 'age_group'] = '10-19'
    admissions.loc[(admissions['age'] >= 20) &
                   (admissions['age'] < 30), 'age_group'] = '20-29'
    admissions.loc[(admissions['age'] >= 30) &
                   (admissions['age'] < 40), 'age_group'] = '30-39'
    admissions.loc[(admissions['age'] >= 40) &
                   (admissions['age'] < 50), 'age_group'] = '40-49'
    admissions.loc[(admissions['age'] >= 50) &
                   (admissions['age'] < 60), 'age_group'] = '50-59'
    admissions.loc[(admissions['age'] >= 60) &
                   (admissions['age'] < 70), 'age_group'] = '60-69'
    admissions.loc[(admissions['age'] >= 70) &
                   (admissions['age'] < 80), 'age_group'] = '70-79'
    admissions.loc[(admissions['age'] >= 80), 'age_group'] = '80+'

    admissions['admittime'] = pd.to_datetime(admissions['admittime'])
    admissions['dischtime'] = pd.to_datetime(admissions['dischtime'])
    admissions['deathtime'] = pd.to_datetime(admissions['deathtime'])

    #make a copy of admissions
    admissions2 = admissions.copy()

    #group future dates into 2001-2012
    admissions2['admit_year'] = pd.Series(np.zeros(admissions2.shape[0]))
    admissions2.loc[admissions2['admittime'].dt.year > 2201, 'admit_year'] = 2012
    admissions2.loc[(admissions2['admittime'].dt.year <= 2201) &
                    (admissions2['admittime'].dt.year > 2192), 'admit_year'] = 2011
    admissions2.loc[(admissions2['admittime'].dt.year <= 2192) &
                    (admissions2['admittime'].dt.year > 2183), 'admit_year'] = 2010
    admissions2.loc[(admissions2['admittime'].dt.year <= 2183) &
                    (admissions2['admittime'].dt.year > 2174), 'admit_year'] = 2009
    admissions2.loc[(admissions2['admittime'].dt.year <= 2174) &
                    (admissions2['admittime'].dt.year > 2165), 'admit_year'] = 2008
    admissions2.loc[(admissions2['admittime'].dt.year <= 2165) &
                    (admissions2['admittime'].dt.year > 2156), 'admit_year'] = 2007
    admissions2.loc[(admissions2['admittime'].dt.year <= 2156) &
                    (admissions2['admittime'].dt.year > 2147), 'admit_year'] = 2006
    admissions2.loc[(admissions2['admittime'].dt.year <= 2147) &
                    (admissions2['admittime'].dt.year > 2138), 'admit_year'] = 2005
    admissions2.loc[(admissions2['admittime'].dt.year <= 2138) &
                    (admissions2['admittime'].dt.year > 2129), 'admit_year'] = 2004
    admissions2.loc[(admissions2['admittime'].dt.year <= 2129) &
                    (admissions2['admittime'].dt.year > 2120), 'admit_year'] = 2003
    admissions2.loc[(admissions2['admittime'].dt.year <= 2120) &
                    (admissions2['admittime'].dt.year > 2111), 'admit_year'] = 2002
    admissions2.loc[admissions2['admittime'].dt.year <= 2111, 'admit_year'] = 2001

    #convert new variable to an integer
    admissions2['admit_year'] = admissions2['admit_year'].astype('int')

    #extract month and date
    admissions2['admit_month'] = admissions2['admittime'].dt.month
    admissions2['admit_day'] = admissions2['admittime'].dt.day

    #convert all leap year days to 2004 to avoid conflict
    admissions2.loc[(admissions2['admit_day'] == 29) &
                    (admissions2['admit_month'] == 2), 'admit_year'] = 2004

    #convert to strings
    admissions2['admit_year'] = admissions2['admit_year'].astype('str')
    admissions2['admit_month'] = admissions2['admit_month'].astype('str')
    admissions2['admit_day'] = admissions2['admit_day'].astype('str')

    #merge new variables
    admissions2['admit_new'] = admissions2[['admit_year', 'admit_month',
                                            'admit_day']].apply(lambda x: '-'.join(x), axis=1)

    #convert string to date
    admissions2['admit_new'] = pd.to_datetime(admissions2['admit_new'])

    #remove all new variables except converted date
    admissions2.drop(['admit_month', 'admit_day'], axis=1, inplace=True)

    #repeating above process for discharge date
    admissions2['disch_year'] = pd.Series(np.zeros(admissions2.shape[0]))
    admissions2.loc[admissions2['dischtime'].dt.year > 2201, 'disch_year'] = 2012
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2201) &
                    (admissions2['dischtime'].dt.year > 2192), 'disch_year'] = 2011
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2192) &
                    (admissions2['dischtime'].dt.year > 2183), 'disch_year'] = 2010
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2183) &
                    (admissions2['dischtime'].dt.year > 2174), 'disch_year'] = 2009
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2174) &
                    (admissions2['dischtime'].dt.year > 2165), 'disch_year'] = 2008
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2165) &
                    (admissions2['dischtime'].dt.year > 2156), 'disch_year'] = 2007
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2156) &
                    (admissions2['dischtime'].dt.year > 2147), 'disch_year'] = 2006
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2147) &
                    (admissions2['dischtime'].dt.year > 2138), 'disch_year'] = 2005
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2138) &
                    (admissions2['dischtime'].dt.year > 2129), 'disch_year'] = 2004
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2129) &
                    (admissions2['dischtime'].dt.year > 2120), 'disch_year'] = 2003
    admissions2.loc[(admissions2['dischtime'].dt.year <= 2120) &
                    (admissions2['dischtime'].dt.year > 2111), 'disch_year'] = 2002
    admissions2.loc[admissions2['dischtime'].dt.year <= 2111, 'disch_year'] = 2001

    #convert to integer
    admissions2['disch_year'] = admissions2['disch_year'].astype('int')

    #extract month and day
    admissions2['disch_month'] = admissions2['dischtime'].dt.month
    admissions2['disch_day'] = admissions2['dischtime'].dt.day

    #converting leap year problems
    admissions2.loc[(admissions2['disch_day'] == 29) &
                    (admissions2['disch_month'] == 2), 'disch_year'] = 2004

    #converting year, month, and day to string for merge
    admissions2['disch_year'] = admissions2['disch_year'].astype('str')
    admissions2['disch_month'] = admissions2['disch_month'].astype('str')
    admissions2['disch_day'] = admissions2['disch_day'].astype('str')

    #merge into one date
    admissions2['disch_new'] = admissions2[['disch_year', 'disch_month',
                                            'disch_day']].apply(lambda x: '-'.join(x), axis=1)

    #convert to datetime
    admissions2['disch_new'] = pd.to_datetime(admissions2['disch_new'])

    #drop excess variables
    admissions2.drop(['disch_year', 'disch_month', 'disch_day'], axis=1, inplace=True)

    return (admissions, admissions2)


def narms_processor(narms):
    """
    cuts down narms data to appropriate US region and condition
    limits columns to only relevant
    reformats columns

    Input: narms: "Isolatedata.csv"
    Output: narms_year: Applied groupby to "Data_Year" and aggregate the other columns
            narms_year_age: Applied groupby to both "Data_year" and "Age_group"
            and aggregate the other columns
    """
    #Select region that corresponds to the MIMIC data
    narms_r1 = narms[narms.Region_Name == 'Region 1']
    #Select only Salmonella
    narms_r1_salm = narms_r1[narms_r1.Genus == 'Salmonella']
    #Cut down narms data
    narms_cut = narms_r1_salm.copy()
    narms_cut = narms_cut.iloc[:, [0, 1, 2, 3, 4, 6, 8, 16, 20, 24, 28, 32, 36, 40, 44, 48,
                                   52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100,
                                   104, 108, 112, 116, 120, 124, 128, 132, 136]]

    #Convert all antibiotics to boolean that indicates resistence detected
    narms_cut['AMI_Concl'] = (narms_cut['AMI_Concl'] == 'R').astype(int)
    narms_cut['AMP_Concl'] = (narms_cut['AMP_Concl'] == 'R').astype(int)
    narms_cut['ATM_Concl'] = (narms_cut['ATM_Concl'] == 'R').astype(int)
    narms_cut['AUG_Concl'] = (narms_cut['AUG_Concl'] == 'R').astype(int)
    narms_cut['AXO_Concl'] = (narms_cut['AXO_Concl'] == 'R').astype(int)
    narms_cut['AZM_Concl'] = (narms_cut['AZM_Concl'] == 'R').astype(int)
    narms_cut['CAZ_Concl'] = (narms_cut['CAZ_Concl'] == 'R').astype(int)
    narms_cut['CCV_Concl'] = (narms_cut['CCV_Concl'] == 'R').astype(int)
    narms_cut['CEP_Concl'] = (narms_cut['CEP_Concl'] == 'R').astype(int)
    narms_cut['CEQ_Concl'] = (narms_cut['CEQ_Concl'] == 'R').astype(int)
    narms_cut['CHL_Concl'] = (narms_cut['CHL_Concl'] == 'R').astype(int)
    narms_cut['CIP_Concl'] = (narms_cut['CIP_Concl'] == 'R').astype(int)
    narms_cut['CLI_Concl'] = (narms_cut['CLI_Concl'] == 'R').astype(int)
    narms_cut['COT_Concl'] = (narms_cut['COT_Concl'] == 'R').astype(int)
    narms_cut['CTC_Concl'] = (narms_cut['CTC_Concl'] == 'R').astype(int)
    narms_cut['CTX_Concl'] = (narms_cut['CTX_Concl'] == 'R').astype(int)
    narms_cut['ERY_Concl'] = (narms_cut['ERY_Concl'] == 'R').astype(int)
    narms_cut['FEP_Concl'] = (narms_cut['FEP_Concl'] == 'R').astype(int)
    narms_cut['FFN_Concl'] = (narms_cut['FFN_Concl'] == 'R').astype(int)
    narms_cut['FIS_Concl'] = (narms_cut['FIS_Concl'] == 'R').astype(int)
    narms_cut['FOX_Concl'] = (narms_cut['FOX_Concl'] == 'R').astype(int)
    narms_cut['GEN_Concl'] = (narms_cut['GEN_Concl'] == 'R').astype(int)
    narms_cut['IMI_Concl'] = (narms_cut['IMI_Concl'] == 'R').astype(int)
    narms_cut['KAN_Concl'] = (narms_cut['KAN_Concl'] == 'R').astype(int)
    narms_cut['NAL_Concl'] = (narms_cut['NAL_Concl'] == 'R').astype(int)
    narms_cut['PTZ_Concl'] = (narms_cut['PTZ_Concl'] == 'R').astype(int)
    narms_cut['SMX_Concl'] = (narms_cut['SMX_Concl'] == 'R').astype(int)
    narms_cut['STR_Concl'] = (narms_cut['STR_Concl'] == 'R').astype(int)
    narms_cut['TEL_Concl'] = (narms_cut['TEL_Concl'] == 'R').astype(int)
    narms_cut['TET_Concl'] = (narms_cut['TET_Concl'] == 'R').astype(int)
    narms_cut['TIO_Concl'] = (narms_cut['TIO_Concl'] == 'R').astype(int)

    cols = ['AMI_Concl', 'AMP_Concl', 'ATM_Concl', 'AUG_Concl', 'AXO_Concl', 'AZM_Concl',
            'CAZ_Concl', 'CCV_Concl', 'CEP_Concl', 'CEQ_Concl', 'CHL_Concl',
            'CIP_Concl', 'CLI_Concl', 'COT_Concl', 'CTC_Concl', 'CTX_Concl',
            'ERY_Concl', 'FEP_Concl', 'FFN_Concl', 'FIS_Concl', 'FOX_Concl',
            'GEN_Concl', 'IMI_Concl', 'KAN_Concl', 'NAL_Concl', 'PTZ_Concl',
            'SMX_Concl', 'STR_Concl', 'TEL_Concl', 'TET_Concl', 'TIO_Concl']
    narms_cut[cols] = narms_cut[cols].replace({0:np.nan})

    #Convert Resistance Pattern
    narms_cut['Resistance_Pattern'] = (narms_cut['Resistance_Pattern'] !=
                                       'No resistance detected').astype(int)
    cols = ['Resistance_Pattern']
    narms_cut[cols] = narms_cut[cols].replace({0:np.nan})


    #Create aggregate information for all resistance per year
    narms_year = narms_cut.groupby(['Data_Year']).agg({'Specimen_ID':'nunique',
                                                       'Resistance_Pattern':"count",
                                                       'AMI_Concl':"count",
                                                       'AMP_Concl':"count",
                                                       'ATM_Concl':"count",
                                                       'AUG_Concl':"count",
                                                       'AXO_Concl':"count",
                                                       'AZM_Concl':"count",
                                                       'CAZ_Concl':"count",
                                                       'CCV_Concl':"count",
                                                       'CEP_Concl':"count",
                                                       'CEQ_Concl':"count",
                                                       'CHL_Concl':"count",
                                                       'CIP_Concl':"count",
                                                       'CLI_Concl':"count",
                                                       'COT_Concl':"count",
                                                       'CTC_Concl':"count",
                                                       'CTX_Concl':"count",
                                                       'ERY_Concl':"count",
                                                       'FEP_Concl':"count",
                                                       'FFN_Concl':"count",
                                                       'FIS_Concl':"count",
                                                       'FOX_Concl':"count",
                                                       'GEN_Concl':"count",
                                                       'IMI_Concl':"count",
                                                       'KAN_Concl':"count",
                                                       'NAL_Concl':"count",
                                                       'PTZ_Concl':"count",
                                                       'SMX_Concl':"count",
                                                       'STR_Concl':"count",
                                                       'TEL_Concl':"count",
                                                       'TET_Concl':"count",
                                                       'TIO_Concl':"count"})


    #Create aggregation for all resistance for a given year & age group
    narms_year_age = narms_cut.groupby(['Data_Year',
                                        'Age_Group']).agg({'Specimen_ID':'nunique',
                                                           'Resistance_Pattern':"count",
                                                           'AMI_Concl':"count",
                                                           'AMP_Concl':"count",
                                                           'ATM_Concl':"count",
                                                           'AUG_Concl':"count",
                                                           'AXO_Concl':"count",
                                                           'AZM_Concl':"count",
                                                           'CAZ_Concl':"count",
                                                           'CCV_Concl':"count",
                                                           'CEP_Concl':"count",
                                                           'CEQ_Concl':"count",
                                                           'CHL_Concl':"count",
                                                           'CIP_Concl':"count",
                                                           'CLI_Concl':"count",
                                                           'COT_Concl':"count",
                                                           'CTC_Concl':"count",
                                                           'CTX_Concl':"count",
                                                           'ERY_Concl':"count",
                                                           'FEP_Concl':"count",
                                                           'FFN_Concl':"count",
                                                           'FIS_Concl':"count",
                                                           'FOX_Concl':"count",
                                                           'GEN_Concl':"count",
                                                           'IMI_Concl':"count",
                                                           'KAN_Concl':"count",
                                                           'NAL_Concl':"count",
                                                           'PTZ_Concl':"count",
                                                           'SMX_Concl':"count",
                                                           'STR_Concl':"count",
                                                           'TEL_Concl':"count",
                                                           'TET_Concl':"count",
                                                           'TIO_Concl':"count"})

    return (narms_year, narms_year_age)

def merge_processor(diagnoses_icd, d_diagnoses_icd, procedures_icd, d_procedures_icd,
                    salmonella_icd, admissions2, drgcodes, prescriptions):
    """
    Merge imported datasets

    Input: diagnoses_icd, d_diagnoses_icd, procedures_icd, d_procedures_icd,
           salmonella_icd, admissions2, drgcodes, prescriptions. They are all
           imported from dataset.
    Output: A file merged all of the imputs.
    """
    #Merge diagnoses with its definitions
    merge_diagnoses = pd.merge(diagnoses_icd.drop(columns=['Unnamed: 0']),
                               d_diagnoses_icd.drop(columns=['Unnamed: 0']), how='inner',
                               left_on='icd9_code', right_on='icd9_code')

    #Merge procedures with its definitions
    merge_procedures = pd.merge(procedures_icd.drop(columns=['Unnamed: 0']),
                                d_procedures_icd.drop(columns=['Unnamed: 0']), how='inner',
                                left_on='icd9_code', right_on='icd9_code')

    #Merge diagnoses and procedures
    merge_diag_proc = [merge_diagnoses, merge_procedures]
    merge_diag_proc = pd.concat(merge_diag_proc)

    #Connect all ICD-9 codes to salmonella trigger codes
    merge_diag_proc_salm = pd.merge(merge_diag_proc, salmonella_icd
                                    , how='inner', left_on='icd9_code'
                                    , right_on='Code')

    #cut down columns
    merge_diag_proc_salm = merge_diag_proc_salm[['subject_id', 'hadm_id',
                                                 'Code', 'Descriptor']]

    #merge cases with all other diagnoses during that visit
    merge_diag_proc_salm = pd.merge(merge_diag_proc_salm, merge_diag_proc,
                                    how='left', left_on=['subject_id', 'hadm_id'],
                                    right_on=['subject_id', 'hadm_id'])

    #merge with admissions
    merge_salm_admit = pd.merge(merge_diag_proc_salm,
                                admissions2.drop(columns=['Unnamed: 0']),
                                how='left', left_on=['subject_id', 'hadm_id'],
                                right_on=['subject_id', 'hadm_id'])

    #merge with drgcodes
    merge_salm_admit_drg = pd.merge(merge_salm_admit, drgcodes.drop(columns=['Unnamed: 0']),
                                    how='left', left_on=['subject_id', 'hadm_id'],
                                    right_on=['subject_id', 'hadm_id'])

    #merge with prescriptions
    merge_all_salmonella = pd.merge(merge_salm_admit_drg,
                                    prescriptions.drop(columns=['Unnamed: 0']),
                                    how='left', left_on=['subject_id', 'hadm_id'],
                                    right_on=['subject_id', 'hadm_id'])

    #cut down columns to other those we'd want in the eCR
    merge_all_salmonella.drop(['admittime', 'dischtime', 'deathtime', 'short_title',
                               'drg_type', 'drg_code', 'icustay_id', 'startdate',
                               'enddate', 'drg_severity', 'drg_mortality', 'row_id',
                               'drug_name_poe', 'drug_name_generic'], axis=1, inplace=True)
    return merge_all_salmonella

def main():
    """
    This function import all of the data, and then made a process for salmonella_tc, admissions
    and narms. The merge everything.
    Output: merges everything
    """
    prescriptions = pd.read_csv("../Data/mimic_prescriptions.csv")
    diagnoses_icd = pd.read_csv("../Data/mimic_diagnoses_icd.csv")
    d_diagnoses_icd = pd.read_csv("../Data/mimic_d_diagnoses_icd.csv")
    admissions = pd.read_csv("../Data/mimic_admissions.csv")
    drgcodes = pd.read_csv("../Data/mimic_drgcodes.csv")
    procedures_icd = pd.read_csv("../Data/mimic_procedures_icd.csv")
    d_procedures_icd = pd.read_csv("../Data/mimic_d_procedures_icd.csv")
    salmonella_tc = pd.read_csv("../Data/salmonellaRCTC.csv")
    narms = pd.read_csv("../Data/IsolateData.csv", low_memory=False)

    salmonella_icd = salmonella_rctc_processor(salmonella_tc)
    #admissions
    admission_list = admissions_processor(admissions)
    admissions = admission_list[0]
    admissions2 = admission_list[1]
    #narms
    narms_proc = narms_processor(narms)
    narms_year = narms_proc[0]
    narms_year_age = narms_proc[1]
    #Merge
    merge_all_salmonella = merge_processor(diagnoses_icd, d_diagnoses_icd, procedures_icd,
                                           d_procedures_icd, salmonella_icd, admissions2,
                                           drgcodes, prescriptions)
    return merge_all_salmonella

if __name__ == '__main__':
    main()
