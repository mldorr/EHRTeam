"""
This file imports necessary data from the local sql database
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# below imports are used to print out pretty pandas dataframes
from IPython.display import display, HTML

%matplotlib inline
plt.style.use('ggplot')

# information used to create a database connection
sqluser = 'postgres'
dbname = 'mimic'
schema_name = 'mimiciii'
pw = 'postgres'

# Connect to postgres with a copy of the MIMIC-III database
con = psycopg2.connect(dbname=dbname, user=sqluser, password=pw)

# the below statement is prepended to queries to ensure they select from the right schema
query_schema = 'set search_path to ' + schema_name + ';'



#get data from table: prescriptions
query = query_schema +"""
SELECT row_id, subject_id, hadm_id, icustay_id, startdate
    , enddate, drug_type, drug, drug_name_poe
    , drug_name_generic, formulary_drug_cd
FROM prescriptions
"""
prescriptions = pd.read_sql_query(query, con)

#get data from table: diagnoses_icd
query = query_schema +"""
SELECT subject_id, hadm_id, icd9_code
FROM diagnoses_icd
"""
diagnoses_icd = pd.read_sql_query(query, con)

#get data from table: d_diagnoses_icd
query = query_schema +"""
SELECT short_title, icd9_code, long_title
FROM d_icd_diagnoses
"""
d_diagnoses_icd = pd.read_sql_query(query, con)

#get data from tables: admissions and patients (+ calculate age)
query = query_schema +"""
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
admissions = pd.read_sql_query(query, con)


#get data from table: drgcodes
query = query_schema +"""
SELECT subject_id, hadm_id, drg_type, drg_code
    , description, drg_severity, drg_mortality
FROM drgcodes
"""
drgcodes = pd.read_sql_query(query, con)


#get icd-9 codes from table: procedures_icd
query = query_schema +"""
SELECT subject_id, hadm_id, icd9_code
FROM procedures_icd
"""
procedures_icd = pd.read_sql_query(query, con)


#get data from table: d_icd_procedures
query = query_schema +"""
SELECT icd9_code, short_title, long_title
FROM d_icd_diagnoses
"""
d_procedures_icd = pd.read_sql_query(query, con)

#get notes
query = query_schema +"""
SELECT subject_id, hadm_id, chartdate, category, description, text
FROM noteevents
"""
notes = pd.read_sql_query(query, con)

#export all to CSVs
prescriptions.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_prescriptions.csv")
diagnoses_icd.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_diagnoses_icd.csv")
d_diagnoses_icd.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_d_diagnoses_icd.csv")
admissions.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_admissions.csv")
drgcodes.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_drgcodes.csv")
procedures_icd.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_procedures_icd.csv")
d_procedures_icd.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_d_procedures_icd.csv")
notes.to_csv("C:/Users/Maggie/OneDrive/UW-BHI/2018Fall/CSE583/Project/mimic_notes.csv")
