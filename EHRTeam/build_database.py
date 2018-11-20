"""
Import all csv files to build database
"""

import numpy as np
import pandas as pd


#Import MIMIC datasets
prescriptions = pd.read_csv("/home/maggie/EHRTeam/Data/mimic_prescriptions.csv")
diagnoses_icd = pd.read_csv("/home/maggie/EHRTeam/Data/mimic_diagnoses_icd.csv")
d_diagnoses_icd = pd.read_csv("/home/maggie/EHRTeam/Data/mimic_d_diagnoses_icd.csv")
admissions = pd.read_csv("/home/maggie/EHRTeam/Data/mimic_admissions.csv")
drgcodes = pd.read_csv("/home/maggie/EHRTeam/Data/mimic_drgcodes.csv")
procedures_icd = pd.read_csv("/home/maggie/EHRTeam/Data/mimic_procedures_icd.csv")
d_procedures_icd = pd.read_csv("/home/maggie/EHRTeam/Data/mimic_d_procedures_icd.csv")

#Import salmonella trigger codes and select only ICD-9 codes
salmonellaTC = pd.read_csv("/home/maggie/EHRTeam/Data/salmonellaRCTC.csv")
salmonellaICD = salmonellaTC[salmonellaTC.CodeSystem=='ICD9CM']


"""
Reprocess dates from random future dates (how the EHR was anonymized)
to match the MIMIC dataframe date range
"""
#make a copy of admissions
admissions2=admissions.copy()

#group future dates into 2001-2012
admissions2['admit_year'] = pd.Series(np.zeros(admissions2.shape[0]))
admissions2.loc[admissions2['admittime'].dt.year>2201, 'admit_year'] = int(2012)
admissions2.loc[(admissions2['admittime'].dt.year<=2201) & (admissions2['admittime'].dt.year>2192), 'admit_year'] = int(2011)
admissions2.loc[(admissions2['admittime'].dt.year<=2192) & (admissions2['admittime'].dt.year>2183), 'admit_year'] = 2010
admissions2.loc[(admissions2['admittime'].dt.year<=2183) & (admissions2['admittime'].dt.year>2174), 'admit_year'] = 2009
admissions2.loc[(admissions2['admittime'].dt.year<=2174) & (admissions2['admittime'].dt.year>2165), 'admit_year'] = 2008
admissions2.loc[(admissions2['admittime'].dt.year<=2165) & (admissions2['admittime'].dt.year>2156), 'admit_year'] = 2007
admissions2.loc[(admissions2['admittime'].dt.year<=2156) & (admissions2['admittime'].dt.year>2147), 'admit_year'] = 2006
admissions2.loc[(admissions2['admittime'].dt.year<=2147) & (admissions2['admittime'].dt.year>2138), 'admit_year'] = 2005
admissions2.loc[(admissions2['admittime'].dt.year<=2138) & (admissions2['admittime'].dt.year>2129), 'admit_year'] = 2004
admissions2.loc[(admissions2['admittime'].dt.year<=2129) & (admissions2['admittime'].dt.year>2120), 'admit_year'] = 2003
admissions2.loc[(admissions2['admittime'].dt.year<=2120) & (admissions2['admittime'].dt.year>2111), 'admit_year'] = 2002
admissions2.loc[admissions2['admittime'].dt.year<=2111, 'admit_year'] = 2001

#convert new variable to an integer
admissions2['admit_year'] = admissions2['admit_year'].astype('int')
#admissions2.head()

#extract month and date
admissions2['admit_month']=admissions2['admittime'].dt.month
admissions2['admit_day']=admissions2['admittime'].dt.day

#convert all leap year days to 2004 to avoid conflict
admissions2.loc[(admissions2['admit_day']==29) & (admissions2['admit_month']==2), 'admit_year'] = 2004

#convert to strings
admissions2['admit_year'] = admissions2['admit_year'].astype('str')
admissions2['admit_month'] = admissions2['admit_month'].astype('str')
admissions2['admit_day'] = admissions2['admit_day'].astype('str')

#merge new variables
admissions2['admit_new']=admissions2[['admit_year', 'admit_month', 'admit_day']].apply(lambda x: '-'.join(x), axis=1)

#convert string to date
admissions2['admit_new'] = pd.to_datetime(admissions2['admit_new'])

#print dataset head
#admissions2.head()

#remove all new variables except converted date
cols=[16,17,18]
admissions2.drop(admissions2.columns[cols], axis=1,inplace=True)

#print dataframe info
#admissions2.info()

#repeating above process for discharge date
admissions2['disch_year'] = pd.Series(np.zeros(admissions2.shape[0]))
admissions2.loc[admissions2['dischtime'].dt.year>2201, 'disch_year'] = 2012
admissions2.loc[(admissions2['dischtime'].dt.year<=2201) & (admissions2['dischtime'].dt.year>2192), 'disch_year'] = 2011
admissions2.loc[(admissions2['dischtime'].dt.year<=2192) & (admissions2['dischtime'].dt.year>2183), 'disch_year'] = 2010
admissions2.loc[(admissions2['dischtime'].dt.year<=2183) & (admissions2['dischtime'].dt.year>2174), 'disch_year'] = 2009
admissions2.loc[(admissions2['dischtime'].dt.year<=2174) & (admissions2['dischtime'].dt.year>2165), 'disch_year'] = 2008
admissions2.loc[(admissions2['dischtime'].dt.year<=2165) & (admissions2['dischtime'].dt.year>2156), 'disch_year'] = 2007
admissions2.loc[(admissions2['dischtime'].dt.year<=2156) & (admissions2['dischtime'].dt.year>2147), 'disch_year'] = 2006
admissions2.loc[(admissions2['dischtime'].dt.year<=2147) & (admissions2['dischtime'].dt.year>2138), 'disch_year'] = 2005
admissions2.loc[(admissions2['dischtime'].dt.year<=2138) & (admissions2['dischtime'].dt.year>2129), 'disch_year'] = 2004
admissions2.loc[(admissions2['dischtime'].dt.year<=2129) & (admissions2['dischtime'].dt.year>2120), 'disch_year'] = 2003
admissions2.loc[(admissions2['dischtime'].dt.year<=2120) & (admissions2['dischtime'].dt.year>2111), 'disch_year'] = 2002
admissions2.loc[admissions2['dischtime'].dt.year<=2111, 'disch_year'] = 2001

admissions2['disch_year'] = admissions2['disch_year'].astype('int')

admissions2['disch_month']=admissions2['dischtime'].dt.month
admissions2['disch_day']=admissions2['dischtime'].dt.day

admissions2.loc[(admissions2['disch_day']==29) & (admissions2['disch_month']==2), 'disch_year'] = 2004

admissions2['disch_year'] = admissions2['disch_year'].astype('str')
admissions2['disch_month'] = admissions2['disch_month'].astype('str')
admissions2['disch_day'] = admissions2['disch_day'].astype('str')

admissions2['disch_new']=admissions2[['disch_year', 'disch_month', 'disch_day']].apply(lambda x: '-'.join(x), axis=1)

admissions2['disch_new'] = pd.to_datetime(admissions2['disch_new'])

cols=[17,18,19]
admissions2.drop(admissions2.columns[cols], axis=1,inplace=True)




"""
Merge imported datasets
"""
#Merge diagnoses with its definitions
merge_diagnoses = pd.merge(diagnoses_icd, d_diagnoses_icd, how='inner', left_on='icd9_code', right_on='icd9_code')

#Merge procedures with its definitions
merge_procedures = pd.merge(procedures_icd, d_procedures_icd, how='inner', left_on='icd9_code', right_on='icd9_code')

#Merge diagnoses and procedures
merge_diag_proc = [merge_diagnoses, merge_procedures]
merge_diag_proc = pd.concat(merge_diag_proc)

#Connect all ICD-9 codes to salmonella trigger codes
merge_diag_proc_salm = pd.merge(merge_diag_proc, salmonellaICD
                                , how='inner', left_on='icd9_code'
                                , right_on='Code')
#cut down columns
merge_diag_proc_salm = merge_diag_proc_salm[['subject_id','hadm_id'
                                             , 'Code', 'Descriptor']]
#merge cases with all other diagnoses during that visit
merge_diag_proc_salm = pd.merge(merge_diag_proc_salm, merge_diag_proc
                               , how='left', left_on=['subject_id', 'hadm_id']
                               , right_on=['subject_id', 'hadm_id'])
#should be 1297 unique

#merge with admissions
merge_salm_admit = pd.merge(merge_diag_proc_salm, admissions2
                               , how='left', left_on=['subject_id', 'hadm_id']
                               , right_on=['subject_id', 'hadm_id'])

#merge with drgcodes
merge_salm_admit_drg = pd.merge(merge_salm_admit, drgcodes
                               , how='left', left_on=['subject_id', 'hadm_id']
                               , right_on=['subject_id', 'hadm_id'])

#merge with prescriptions
merge_all_salmonella = pd.merge(merge_salm_admit_drg, prescriptions
                               , how='left', left_on=['subject_id', 'hadm_id']
                               , right_on=['subject_id', 'hadm_id'])



