"""
database_build

used to import and merge dataframes
"""

import numpy as np
import pandas as pd
import os

def salmonellaRCTC_processor(SALMONELLA_TC):
    """selects only ICD-9 salmonella trigger codes"""
    SALMONELLA_ICD = SALMONELLA_TC[SALMONELLA_TC.CodeSystem == 'ICD9CM']
    return SALMONELLA_ICD

def admissions_processor(ADMISSIONS):
    """
    creates age_group variable and reprocesses dates from random
    future dates (how the EHR was anonymized) to match the MIMIC
    dataframe date range
    """
    ADMISSIONS['age_group'] = pd.Series(np.zeros(ADMISSIONS.shape[0]))
    ADMISSIONS.loc[(ADMISSIONS['age'] > 0) &
                   (ADMISSIONS['age'] < 5), 'age_group'] = '0-4'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 5) &
                   (ADMISSIONS['age'] < 10), 'age_group'] = '5-9'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 10) &
                   (ADMISSIONS['age'] < 20), 'age_group'] = '10-19'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 20) &
                   (ADMISSIONS['age'] < 30), 'age_group'] = '20-29'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 30) &
                   (ADMISSIONS['age'] < 40), 'age_group'] = '30-39'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 40) &
                   (ADMISSIONS['age'] < 50), 'age_group'] = '40-49'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 50) &
                   (ADMISSIONS['age'] < 60), 'age_group'] = '50-59'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 60) &
                   (ADMISSIONS['age'] < 70), 'age_group'] = '60-69'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 70) &
                   (ADMISSIONS['age'] < 80), 'age_group'] = '70-79'
    ADMISSIONS.loc[(ADMISSIONS['age'] >= 80), 'age_group'] = '80+'

    ADMISSIONS['admittime'] = pd.to_datetime(ADMISSIONS['admittime'])
    ADMISSIONS['dischtime'] = pd.to_datetime(ADMISSIONS['dischtime'])
    ADMISSIONS['deathtime'] = pd.to_datetime(ADMISSIONS['deathtime'])

    #make a copy of ADMISSIONS
    ADMISSIONS2 = ADMISSIONS.copy()

    #group future dates into 2001-2012
    ADMISSIONS2['admit_year'] = pd.Series(np.zeros(ADMISSIONS2.shape[0]))
    ADMISSIONS2.loc[ADMISSIONS2['admittime'].dt.year > 2201, 'admit_year'] = 2012
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2201) &
                    (ADMISSIONS2['admittime'].dt.year > 2192), 'admit_year'] = 2011
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2192) &
                    (ADMISSIONS2['admittime'].dt.year > 2183), 'admit_year'] = 2010
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2183) &
                    (ADMISSIONS2['admittime'].dt.year > 2174), 'admit_year'] = 2009
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2174) &
                    (ADMISSIONS2['admittime'].dt.year > 2165), 'admit_year'] = 2008
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2165) &
                    (ADMISSIONS2['admittime'].dt.year > 2156), 'admit_year'] = 2007
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2156) &
                    (ADMISSIONS2['admittime'].dt.year > 2147), 'admit_year'] = 2006
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2147) &
                    (ADMISSIONS2['admittime'].dt.year > 2138), 'admit_year'] = 2005
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2138) &
                    (ADMISSIONS2['admittime'].dt.year > 2129), 'admit_year'] = 2004
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2129) &
                    (ADMISSIONS2['admittime'].dt.year > 2120), 'admit_year'] = 2003
    ADMISSIONS2.loc[(ADMISSIONS2['admittime'].dt.year <= 2120) &
                    (ADMISSIONS2['admittime'].dt.year > 2111), 'admit_year'] = 2002
    ADMISSIONS2.loc[ADMISSIONS2['admittime'].dt.year <= 2111, 'admit_year'] = 2001

    #convert new variable to an integer
    ADMISSIONS2['admit_year'] = ADMISSIONS2['admit_year'].astype('int')

    #extract month and date
    ADMISSIONS2['admit_month'] = ADMISSIONS2['admittime'].dt.month
    ADMISSIONS2['admit_day'] = ADMISSIONS2['admittime'].dt.day

    #convert all leap year days to 2004 to avoid conflict
    ADMISSIONS2.loc[(ADMISSIONS2['admit_day'] == 29) &
                    (ADMISSIONS2['admit_month'] == 2), 'admit_year'] = 2004

    #convert to strings
    ADMISSIONS2['admit_year'] = ADMISSIONS2['admit_year'].astype('str')
    ADMISSIONS2['admit_month'] = ADMISSIONS2['admit_month'].astype('str')
    ADMISSIONS2['admit_day'] = ADMISSIONS2['admit_day'].astype('str')

    #merge new variables
    ADMISSIONS2['admit_new'] = ADMISSIONS2[['admit_year', 'admit_month',
                                            'admit_day']].apply(lambda x: '-'.join(x), axis=1)

    #convert string to date
    ADMISSIONS2['admit_new'] = pd.to_datetime(ADMISSIONS2['admit_new'])

    #remove all new variables except converted date
    ADMISSIONS2.drop(['admit_month', 'admit_day'], axis=1, inplace=True)
    #keeping admit_year to match with NARMS


    #repeating above process for discharge date
    ADMISSIONS2['disch_year'] = pd.Series(np.zeros(ADMISSIONS2.shape[0]))
    ADMISSIONS2.loc[ADMISSIONS2['dischtime'].dt.year > 2201, 'disch_year'] = 2012
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2201) &
                    (ADMISSIONS2['dischtime'].dt.year > 2192), 'disch_year'] = 2011
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2192) &
                    (ADMISSIONS2['dischtime'].dt.year > 2183), 'disch_year'] = 2010
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2183) &
                    (ADMISSIONS2['dischtime'].dt.year > 2174), 'disch_year'] = 2009
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2174) &
                    (ADMISSIONS2['dischtime'].dt.year > 2165), 'disch_year'] = 2008
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2165) &
                    (ADMISSIONS2['dischtime'].dt.year > 2156), 'disch_year'] = 2007
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2156) &
                    (ADMISSIONS2['dischtime'].dt.year > 2147), 'disch_year'] = 2006
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2147) &
                    (ADMISSIONS2['dischtime'].dt.year > 2138), 'disch_year'] = 2005
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2138) &
                    (ADMISSIONS2['dischtime'].dt.year > 2129), 'disch_year'] = 2004
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2129) &
                    (ADMISSIONS2['dischtime'].dt.year > 2120), 'disch_year'] = 2003
    ADMISSIONS2.loc[(ADMISSIONS2['dischtime'].dt.year <= 2120) &
                    (ADMISSIONS2['dischtime'].dt.year > 2111), 'disch_year'] = 2002
    ADMISSIONS2.loc[ADMISSIONS2['dischtime'].dt.year <= 2111, 'disch_year'] = 2001

    ADMISSIONS2['disch_year'] = ADMISSIONS2['disch_year'].astype('int')

    ADMISSIONS2['disch_month'] = ADMISSIONS2['dischtime'].dt.month
    ADMISSIONS2['disch_day'] = ADMISSIONS2['dischtime'].dt.day

    ADMISSIONS2.loc[(ADMISSIONS2['disch_day'] == 29) &
                    (ADMISSIONS2['disch_month'] == 2), 'disch_year'] = 2004

    ADMISSIONS2['disch_year'] = ADMISSIONS2['disch_year'].astype('str')
    ADMISSIONS2['disch_month'] = ADMISSIONS2['disch_month'].astype('str')
    ADMISSIONS2['disch_day'] = ADMISSIONS2['disch_day'].astype('str')

    ADMISSIONS2['disch_new'] = ADMISSIONS2[['disch_year', 'disch_month',
                                            'disch_day']].apply(lambda x: '-'.join(x), axis=1)

    ADMISSIONS2['disch_new'] = pd.to_datetime(ADMISSIONS2['disch_new'])

    ADMISSIONS2.drop(['disch_year', 'disch_month', 'disch_day'], axis=1, inplace=True)

    return (ADMISSIONS, ADMISSIONS2)

def narms_processor(NARMS):
    """
    cuts down narms data to appropriate US region and condition
    limits columns to only relevant
    reformats columns
    """
    #Select region that corresponds to the MIMIC data
    NARMS_R1 = NARMS[NARMS.Region_Name == 'Region 1']
    #Select only Salmonella
    NARMS_R1_SALM = NARMS_R1[NARMS_R1.Genus == 'Salmonella']
    #Cut down narms data
    NARMS_CUT = NARMS_R1_SALM.copy()
    NARMS_CUT = NARMS_CUT.iloc[:, [0, 1, 2, 3, 4, 6, 8, 16, 20, 24, 28, 32, 36, 40, 44, 48,
                                   52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100,
                                   104, 108, 112, 116, 120, 124, 128, 132, 136]]

    #Convert all antibiotics to boolean that indicates resistence detected
    NARMS_CUT['AMI_Concl'] = (NARMS_CUT['AMI_Concl'] == 'R').astype(int)
    NARMS_CUT['AMP_Concl'] = (NARMS_CUT['AMP_Concl'] == 'R').astype(int)
    NARMS_CUT['ATM_Concl'] = (NARMS_CUT['ATM_Concl'] == 'R').astype(int)
    NARMS_CUT['AUG_Concl'] = (NARMS_CUT['AUG_Concl'] == 'R').astype(int)
    NARMS_CUT['AXO_Concl'] = (NARMS_CUT['AXO_Concl'] == 'R').astype(int)
    NARMS_CUT['AZM_Concl'] = (NARMS_CUT['AZM_Concl'] == 'R').astype(int)
    NARMS_CUT['CAZ_Concl'] = (NARMS_CUT['CAZ_Concl'] == 'R').astype(int)
    NARMS_CUT['CCV_Concl'] = (NARMS_CUT['CCV_Concl'] == 'R').astype(int)
    NARMS_CUT['CEP_Concl'] = (NARMS_CUT['CEP_Concl'] == 'R').astype(int)
    NARMS_CUT['CEQ_Concl'] = (NARMS_CUT['CEQ_Concl'] == 'R').astype(int)
    NARMS_CUT['CHL_Concl'] = (NARMS_CUT['CHL_Concl'] == 'R').astype(int)
    NARMS_CUT['CIP_Concl'] = (NARMS_CUT['CIP_Concl'] == 'R').astype(int)
    NARMS_CUT['CLI_Concl'] = (NARMS_CUT['CLI_Concl'] == 'R').astype(int)
    NARMS_CUT['COT_Concl'] = (NARMS_CUT['COT_Concl'] == 'R').astype(int)
    NARMS_CUT['CTC_Concl'] = (NARMS_CUT['CTC_Concl'] == 'R').astype(int)
    NARMS_CUT['CTX_Concl'] = (NARMS_CUT['CTX_Concl'] == 'R').astype(int)
    NARMS_CUT['ERY_Concl'] = (NARMS_CUT['ERY_Concl'] == 'R').astype(int)
    NARMS_CUT['FEP_Concl'] = (NARMS_CUT['FEP_Concl'] == 'R').astype(int)
    NARMS_CUT['FFN_Concl'] = (NARMS_CUT['FFN_Concl'] == 'R').astype(int)
    NARMS_CUT['FIS_Concl'] = (NARMS_CUT['FIS_Concl'] == 'R').astype(int)
    NARMS_CUT['FOX_Concl'] = (NARMS_CUT['FOX_Concl'] == 'R').astype(int)
    NARMS_CUT['GEN_Concl'] = (NARMS_CUT['GEN_Concl'] == 'R').astype(int)
    NARMS_CUT['IMI_Concl'] = (NARMS_CUT['IMI_Concl'] == 'R').astype(int)
    NARMS_CUT['KAN_Concl'] = (NARMS_CUT['KAN_Concl'] == 'R').astype(int)
    NARMS_CUT['NAL_Concl'] = (NARMS_CUT['NAL_Concl'] == 'R').astype(int)
    NARMS_CUT['PTZ_Concl'] = (NARMS_CUT['PTZ_Concl'] == 'R').astype(int)
    NARMS_CUT['SMX_Concl'] = (NARMS_CUT['SMX_Concl'] == 'R').astype(int)
    NARMS_CUT['STR_Concl'] = (NARMS_CUT['STR_Concl'] == 'R').astype(int)
    NARMS_CUT['TEL_Concl'] = (NARMS_CUT['TEL_Concl'] == 'R').astype(int)
    NARMS_CUT['TET_Concl'] = (NARMS_CUT['TET_Concl'] == 'R').astype(int)
    NARMS_CUT['TIO_Concl'] = (NARMS_CUT['TIO_Concl'] == 'R').astype(int)

    COLS = ['AMI_Concl', 'AMP_Concl', 'ATM_Concl', 'AUG_Concl', 'AXO_Concl', 'AZM_Concl',
            'CAZ_Concl', 'CCV_Concl', 'CEP_Concl', 'CEQ_Concl', 'CHL_Concl',
            'CIP_Concl', 'CLI_Concl', 'COT_Concl', 'CTC_Concl', 'CTX_Concl',
            'ERY_Concl', 'FEP_Concl', 'FFN_Concl', 'FIS_Concl', 'FOX_Concl',
            'GEN_Concl', 'IMI_Concl', 'KAN_Concl', 'NAL_Concl', 'PTZ_Concl',
            'SMX_Concl', 'STR_Concl', 'TEL_Concl', 'TET_Concl', 'TIO_Concl']
    NARMS_CUT[COLS] = NARMS_CUT[COLS].replace({0:np.nan})

    #Convert Resistance Pattern
    NARMS_CUT['Resistance_Pattern'] = (NARMS_CUT['Resistance_Pattern'] !=
                                      'No resistance detected').astype(int)
    COLS = ['Resistance_Pattern']
    NARMS_CUT[COLS] = NARMS_CUT[COLS].replace({0:np.nan})


    #Create aggregate information for all resistance per year
    NARMS_YEAR = NARMS_CUT.groupby(['Data_Year']).agg({'Specimen_ID':'nunique',
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
    NARMS_YEAR_AGE = NARMS_CUT.groupby(['Data_Year', 'Age_Group']).agg({'Specimen_ID':'nunique',
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


    #########################################################################
    #This part will need to be modified because it subsets to a specific
    #year and age group, which should match to the patient's year + age
    #but this is what I have for now
    ###################################
    #NARMS_YEAR1 = NARMS_YEAR.query('Data_Year == 2008')
    #NARMS_YEAR_AGE1 = NARMS_YEAR_AGE.query('Data_Year == 2008 & Age_Group == "0-4"')

    #Build a table with the above information
    #FRAMES = [NARMS_YEAR1, NARMS_YEAR_AGE1]
    #NARMS_PATIENT = pd.concat(FRAMES, sort=true)

    return (NARMS_YEAR, NARMS_YEAR_AGE)

def merge_processor(DIAGNOSES_ICD, D_DIAGNOSES_ICD, PROCEDURES_ICD, D_PROCEDURES_ICD,
                    SALMONELLA_ICD, ADMISSIONS2, DRGCODES, PRESCRIPTIONS):
    """
    Merge imported datasets
    """
    print('header', list(DIAGNOSES_ICD.columns.values))

    #Merge diagnoses with its definitions
    MERGE_DIAGNOSES = pd.merge(DIAGNOSES_ICD.drop(columns=['Unnamed: 0']),
                               D_DIAGNOSES_ICD.drop(columns=['Unnamed: 0']), how='inner',
                               left_on='icd9_code', right_on='icd9_code')

    #Merge procedures with its definitions
    MERGE_PROCEDURES = pd.merge(PROCEDURES_ICD.drop(columns=['Unnamed: 0']),
                                D_PROCEDURES_ICD.drop(columns=['Unnamed: 0']), how='inner',
                                left_on='icd9_code', right_on='icd9_code')

    #Merge diagnoses and procedures
    MERGE_DIAG_PROC = [MERGE_DIAGNOSES, MERGE_PROCEDURES]
    MERGE_DIAG_PROC = pd.concat(MERGE_DIAG_PROC)

    #Connect all ICD-9 codes to salmonella trigger codes
    MERGE_DIAG_PROC_SALM = pd.merge(MERGE_DIAG_PROC, SALMONELLA_ICD
                                    , how='inner', left_on='icd9_code'
                                    , right_on='Code')

    #cut down columns
    MERGE_DIAG_PROC_SALM = MERGE_DIAG_PROC_SALM[['subject_id', 'hadm_id',
                                                 'Code', 'Descriptor']]

    #merge cases with all other diagnoses during that visit
    MERGE_DIAG_PROC_SALM = pd.merge(MERGE_DIAG_PROC_SALM, MERGE_DIAG_PROC,
                                    how='left', left_on=['subject_id', 'hadm_id'],
                                    right_on=['subject_id', 'hadm_id'])
    #should be 1297 unique

    #merge with ADMISSIONS
    MERGE_SALM_ADMIT = pd.merge(MERGE_DIAG_PROC_SALM,
                                ADMISSIONS2.drop(columns=['Unnamed: 0']),
                                how='left', left_on=['subject_id', 'hadm_id'],
                                right_on=['subject_id', 'hadm_id'])

    #merge with DRGCODES
    MERGE_SALM_ADMIT_DRG = pd.merge(MERGE_SALM_ADMIT, DRGCODES.drop(columns=['Unnamed: 0']),
                                    how='left', left_on=['subject_id', 'hadm_id'],
                                    right_on=['subject_id', 'hadm_id'])

    #merge with prescriptions
    MERGE_ALL_SALMONELLA = pd.merge(MERGE_SALM_ADMIT_DRG, PRESCRIPTIONS.drop(columns=['Unnamed: 0']),
                                    how='left', left_on=['subject_id', 'hadm_id'],
                                    right_on=['subject_id', 'hadm_id'])

    #cut down columns to other those we'd want in the eCR
    MERGE_ALL_SALMONELLA.drop(['admittime', 'dischtime', 'deathtime', 'short_title',
                               'drg_type', 'drg_code', 'icustay_id', 'startdate',
                               'enddate', 'drg_severity', 'drg_mortality', 'row_id',
                               'drug_name_poe', 'drug_name_generic'], axis=1, inplace=True)
    return MERGE_ALL_SALMONELLA

def main():
    """merges everything"""
    PRESCRIPTIONS = pd.read_csv("../Data/mimic_prescriptions.csv")
    DIAGNOSES_ICD = pd.read_csv("../Data/mimic_diagnoses_icd.csv")
    D_DIAGNOSES_ICD = pd.read_csv("../Data/mimic_d_diagnoses_icd.csv")
    ADMISSIONS = pd.read_csv("../Data/mimic_admissions.csv")
    DRGCODES = pd.read_csv("../Data/mimic_drgcodes.csv")
    PROCEDURES_ICD = pd.read_csv("../Data/mimic_procedures_icd.csv")
    D_PROCEDURES_ICD = pd.read_csv("../Data/mimic_d_procedures_icd.csv")
    SALMONELLA_TC = pd.read_csv("../Data/salmonellaRCTC.csv")
    NARMS = pd.read_csv("../Data/IsolateData.csv", low_memory=False)

    SALMONELLA_ICD = salmonellaRCTC_processor(SALMONELLA_TC)
    #Admissions
    ADMISSION_LIST = admissions_processor(ADMISSIONS)
    ADMISSIONS = ADMISSION_LIST[0]
    ADMISSIONS2 = ADMISSION_LIST[1]
    #NARMS
    NARMS_PROC = narms_processor(NARMS)
    NARMS_YEAR = NARMS_PROC[0]
    NARMS_YEAR_AGE = NARMS_PROC[1]
    #Merge
    MERGE_ALL_SALMONELLA = merge_processor(DIAGNOSES_ICD, D_DIAGNOSES_ICD, PROCEDURES_ICD,
                                           D_PROCEDURES_ICD, SALMONELLA_ICD, ADMISSIONS2,
                                           DRGCODES, PRESCRIPTIONS)
    print('database creation successful')
    MERGE_ALL_SALMONELLA.to_csv('../Data/out.csv')

if __name__ == '__main__':
    main()
