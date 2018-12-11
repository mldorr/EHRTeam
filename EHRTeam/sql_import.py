"""
This file imported the necessary data from the local sql database.
It is not used in the package/module but is included for posterity.
"""

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

plt.style.use('ggplot')

# information used to create a database connection
SQLUSER = 'postgres'
DBNAME = 'mimic'
SCHEMA_NAME = 'mimiciii'
PW = 'postgres'

# Connect to postgres with a copy of the MIMIC-III database
CON = psycopg2.connect(dbname=DBNAME, user=SQLUSER, password=PW)

# the below statement is prepended to queries to ensure they select from the right schema
QUERY_SCHEMA = 'set search_path to ' + SCHEMA_NAME + ';'


#get data from table: prescriptions
QUERY = QUERY_SCHEMA +"""
SELECT row_id, subject_id, hadm_id, icustay_id, startdate
    , enddate, drug_type, drug, drug_name_poe
    , drug_name_generic, formulary_drug_cd
FROM prescriptions
"""
PRESCRIPTIONS = pd.read_sql_query(QUERY, CON)

#get data from table: diagnoses_icd
QUERY = QUERY_SCHEMA +"""
SELECT subject_id, hadm_id, icd9_code
FROM diagnoses_icd
"""
DIAGNOSES_ICD = pd.read_sql_query(QUERY, CON)

#get data from table: d_diagnoses_icd
QUERY = QUERY_SCHEMA +"""
SELECT short_title, icd9_code, long_title
FROM d_icd_diagnoses
"""
D_DIAGNOSES_ICD = pd.read_sql_query(QUERY, CON)

#get data from tables: admissions and patients (+ calculate age)
QUERY = QUERY_SCHEMA +"""
(
SELECT adm.subject_id, adm.hadm_id, adm.admission_type
    , adm.diagnosis, adm.admittime, adm.dischtime, adm.deathtime
    , adm.insurance, adm.language, adm.religion
    , adm.marital_status, adm.ethnicity, pat.gender, pat.expire_flag
    , EXTRACT('epoch' from adm.admittime - pat.dob)  / 60.0 / 60.0 / 24.0 / 365.242 AS age
    , EXTRACT('epoch' from pat.dod - pat.dob)  / 60.0 / 60.0 / 24.0 / 365.242 AS age_death
FROM admissions adm
INNER JOIN patients pat
    ON adm.subject_id = pat.subject_ID
)
"""
ADMISSIONS = pd.read_sql_query(QUERY, CON)

#get data from table: drgcodes
QUERY = QUERY_SCHEMA +"""
SELECT subject_id, hadm_id, drg_type, drg_code
    , description, drg_severity, drg_mortality
FROM drgcodes
"""
DRGCODES = pd.read_sql_query(QUERY, CON)

#get icd-9 codes from table: procedures_icd
QUERY = QUERY_SCHEMA +"""
SELECT subject_id, hadm_id, icd9_code
FROM procedures_icd
"""
PROCEDURES_ICD = pd.read_sql_query(QUERY, CON)

#get data from table: d_icd_procedures
QUERY = QUERY_SCHEMA +"""
SELECT icd9_code, short_title, long_title
FROM d_icd_diagnoses
"""
D_PROCEDURES_ICD = pd.read_sql_query(QUERY, CON)

#get notes
QUERY = QUERY_SCHEMA +"""
SELECT subject_id, hadm_id, chartdate, category, description, text
FROM noteevents
"""
NOTES = pd.read_sql_query(QUERY, CON)

#export all to CSVs
PRESCRIPTIONS.to_csv("C:/Users/Maggie/OneDrive/\
UW-BHI/2018Fall/CSE583/Project/mimic_prescriptions.csv")
DIAGNOSES_ICD.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/\
Project/mimic_diagnoses_icd.csv")
D_DIAGNOSES_ICD.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/\
CSE583/Project/mimic_d_diagnoses_icd.csv")
ADMISSIONS.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_admissions.csv")
DRGCODES.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_drgcodes.csv")
PROCEDURES_ICD.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/\
CSE583/Project/mimic_procedures_icd.csv")
D_PROCEDURES_ICD.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/\
CSE583/Project/mimic_d_procedures_icd.csv")
NOTES.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_notes.csv")
