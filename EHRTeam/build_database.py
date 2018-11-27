"""
Import all csv files and build database
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

#Import NARMS data
NARMS = pd.read_csv("/home/maggie/EHRTeam/Data/IsolateData.csv", low_memory=False)
#Select region that corresponds to the MIMIC data
NARMS_R1 = NARMS[NARMS.Region_Name=='Region 1']
#Select only Salmonella
NARMS_R1_Salm = NARMS_R1[NARMS_R1.Genus=='Salmonella']


#convert time variables to datatime (bc apparently moving them to my subsystem messed that up)
admissions['admittime'] = pd.to_datetime(admissions['admittime'])
admissions['dischtime'] = pd.to_datetime(admissions['dischtime'])
admissions['deathtime'] = pd.to_datetime(admissions['deathtime'])


"""
Reprocess dates from random future dates (how the EHR was anonymized)
to match the MIMIC dataframe date range
"""

#convert time variables to datatime (bc apparently moving them to my subsystem messed that up)
admissions['admittime'] = pd.to_datetime(admissions['admittime'])
admissions['dischtime'] = pd.to_datetime(admissions['dischtime'])
admissions['deathtime'] = pd.to_datetime(admissions['deathtime'])
#admissions.info()

#make a copy of admissions
admissions2=admissions.copy()

#group future dates into 2001-2012
admissions2['admit_year'] = pd.Series(np.zeros(admissions2.shape[0]))
admissions2.loc[admissions2['admittime'].dt.year>2201, 'admit_year'] = 2012
admissions2.loc[(admissions2['admittime'].dt.year<=2201) & (admissions2['admittime'].dt.year>2192), 'admit_year'] = 2011
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
Create NARMS subset for patients
"""
#Cut down narms data
NARMS_cut = NARMS_R1_Salm.copy()
NARMS_cut = NARMS_cut.iloc[:,[0,1,2,3,4,6,8,16,20,24,28,32,36,40,44,48,
                              52,56,60,64,68,72,76,80,84,88,92,96,100,
                             104,108,112,116,120,124,128,132,136]]

#Convert all antibiotics to boolean that indicates resistence detected
NARMS_cut['AMI_Concl'] = (NARMS_cut['AMI_Concl']=='R').astype(int)
NARMS_cut['AMP_Concl'] = (NARMS_cut['AMP_Concl']=='R').astype(int)
NARMS_cut['ATM_Concl'] = (NARMS_cut['ATM_Concl']=='R').astype(int)
NARMS_cut['AUG_Concl'] = (NARMS_cut['AUG_Concl']=='R').astype(int)
NARMS_cut['AXO_Concl'] = (NARMS_cut['AXO_Concl']=='R').astype(int)
NARMS_cut['AZM_Concl'] = (NARMS_cut['AZM_Concl']=='R').astype(int)
NARMS_cut['CAZ_Concl'] = (NARMS_cut['CAZ_Concl']=='R').astype(int)
NARMS_cut['CCV_Concl'] = (NARMS_cut['CCV_Concl']=='R').astype(int)
NARMS_cut['CEP_Concl'] = (NARMS_cut['CEP_Concl']=='R').astype(int)
NARMS_cut['CEQ_Concl'] = (NARMS_cut['CEQ_Concl']=='R').astype(int)
NARMS_cut['CHL_Concl'] = (NARMS_cut['CHL_Concl']=='R').astype(int)
NARMS_cut['CIP_Concl'] = (NARMS_cut['CIP_Concl']=='R').astype(int)
NARMS_cut['CLI_Concl'] = (NARMS_cut['CLI_Concl']=='R').astype(int)
NARMS_cut['COT_Concl'] = (NARMS_cut['COT_Concl']=='R').astype(int)
NARMS_cut['CTC_Concl'] = (NARMS_cut['CTC_Concl']=='R').astype(int)
NARMS_cut['CTX_Concl'] = (NARMS_cut['CTX_Concl']=='R').astype(int)
NARMS_cut['ERY_Concl'] = (NARMS_cut['ERY_Concl']=='R').astype(int)
NARMS_cut['FEP_Concl'] = (NARMS_cut['FEP_Concl']=='R').astype(int)
NARMS_cut['FFN_Concl'] = (NARMS_cut['FFN_Concl']=='R').astype(int)
NARMS_cut['FIS_Concl'] = (NARMS_cut['FIS_Concl']=='R').astype(int)
NARMS_cut['FOX_Concl'] = (NARMS_cut['FOX_Concl']=='R').astype(int)
NARMS_cut['GEN_Concl'] = (NARMS_cut['GEN_Concl']=='R').astype(int)
NARMS_cut['IMI_Concl'] = (NARMS_cut['IMI_Concl']=='R').astype(int)
NARMS_cut['KAN_Concl'] = (NARMS_cut['KAN_Concl']=='R').astype(int)
NARMS_cut['NAL_Concl'] = (NARMS_cut['NAL_Concl']=='R').astype(int)
NARMS_cut['PTZ_Concl'] = (NARMS_cut['PTZ_Concl']=='R').astype(int)
NARMS_cut['SMX_Concl'] = (NARMS_cut['SMX_Concl']=='R').astype(int)
NARMS_cut['STR_Concl'] = (NARMS_cut['STR_Concl']=='R').astype(int)
NARMS_cut['TEL_Concl'] = (NARMS_cut['TEL_Concl']=='R').astype(int)
NARMS_cut['TET_Concl'] = (NARMS_cut['TET_Concl']=='R').astype(int)
NARMS_cut['TIO_Concl'] = (NARMS_cut['TIO_Concl']=='R').astype(int)

cols = ['AMI_Concl','AMP_Concl','ATM_Concl','AUG_Concl', 'AXO_Concl', 'AZM_Concl',
        'CAZ_Concl', 'CCV_Concl', 'CEP_Concl', 'CEQ_Concl', 'CHL_Concl',
        'CIP_Concl', 'CLI_Concl', 'COT_Concl', 'CTC_Concl', 'CTX_Concl',
        'ERY_Concl', 'FEP_Concl', 'FFN_Concl', 'FIS_Concl', 'FOX_Concl',
        'GEN_Concl', 'IMI_Concl', 'KAN_Concl', 'NAL_Concl', 'PTZ_Concl',
        'SMX_Concl', 'STR_Concl', 'TEL_Concl', 'TET_Concl', 'TIO_Concl']
NARMS_cut[cols] = NARMS_cut[cols].replace({0:np.nan})

#Convert Resistance Pattern
NARMS_cut['Resistance_Pattern'] = (NARMS_cut['Resistance_Pattern']!='No resistance detected').astype(int)
cols=['Resistance_Pattern']
NARMS_cut[cols] = NARMS_cut[cols].replace({0:np.nan})


#Create aggregate information for all resistance per year
NARMS_year = NARMS_cut.groupby(['Data_Year']).agg({'Specimen_ID':'nunique',
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
NARMS_year_age = NARMS_cut.groupby(['Data_Year','Age_Group']).agg({'Specimen_ID':'nunique',
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
NARMS_year1 = NARMS_year.query('Data_Year==2008')
NARMS_year_age1 = NARMS_year_age.query('Data_Year==2008 & Age_Group=="0-4"')

#Build a table with the above information
frames = [NARMS_year1, NARMS_year_age1]
NARMS_patient = pd.concat(frames, sort=True)

###########################################################################





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
