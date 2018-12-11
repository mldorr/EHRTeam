from database_build import salmonella_rctc_processor, admissions_processor, narms_processor, merge_processor
import unittest
import pandas as pd
import numpy as np

class TestFunctions(unittest.TestCase):
    """
    Unittest class
    """
    def test_salmonella_rctc_processor(self):
        """ Check if the function select only ICD-9 salmonella trigger codes."""
        if salmonella_icd['CodeSystem'].any() != 'ICD9CM':
            self.test_result = False
        else:
            self.test_result = True
        assert self.test_result == True

    def test_age_group(self):
        """ Check if the year is in the range of 2001 - 2012."""
        self.age_year = admissions2['age_group']
        if isinstance(self.age_year, int):
	        self.test_result = False
        else:
            self.test_result = True
        assert self.test_result == True

    def test_admit_group_year(self):
        """ Check if the year is in the range of 2001 - 2012."""
        self.year_subset = admissions2['admit_new'].dt.year
        if (self.year_subset < 2001).any() and (self.year_subset > 2012).any():
	        self.test_result = False
        else:
            self.test_result = True
        assert self.test_result == True


    def test_disch_group_year(self):
        """ Check if the year is in the range of 2001 - 2012."""
        self.year_subset = admissions2['disch_new'].dt.year
        if (self.year_subset < 2001).any() and (self.year_subset > 2012).any():
            self.test_result = False
        else:
            self.test_result = True
        assert self.test_result == True


    def test_check_admit_columns(self):
        """ Check if the 'admit_year','admit_month','admit_day' columns are deleted."""
        if ('admit_month' in admissions2.columns) or ('admit_day' in admissions2.columns):
            self.test_result = False
        else:
            self.test_result = True
        assert self.test_result == True


    def test_check_disch_columns(self):
        """ Check if the 'disch_year','disch_month','disch_day' columns are deleted."""
        if ('disch_year' in admissions2.columns) or ('disch_month' in admissions2.columns) or ('disch_day' in admissions2.columns):
            self.test_result = False
        else:
            self.test_result = True
        assert self.test_result == True


    def test_narms_processor(self):
        """ Check if the 'narms_year' & 'narms_year_age' have the narms columns that we wanted."""
        if ('Data_Year', 'Specimen_ID', 'Resistance_Pattern', 'AMI_Concl', 'AMP_Concl',
        	'ATM_Concl', 'AUG_Concl', 'AXO_Concl', 'AZM_Concl', 'CAZ_Concl', 'CCV_Concl', 'CEP_Concl',
        	'CEQ_Concl', 'CHL_Concl', 'CIP_Concl', 'CLI_Concl', 'COT_Concl', 'CTC_Concl', 'CTX_Concl',
        	'ERY_Concl', 'FEP_Concl', 'FFN_Concl', 'FIS_Concl', 'FOX_Concl', 'GEN_Concl', 'IMI_Concl',
        	'KAN_Concl', 'NAL_Concl', 'PTZ_Concl', 'SMX_Concl', 'STR_Concl', 'TEL_Concl', 'TET_Concl',
        	'TIO_Concl' in narms_year.columns) and len(narms_year.columns) == 33:
            self.test_result_1 = True
        else:
            self.test_result_1 = False

        if ('Data_Year', 'Age_Group', 'Specimen_ID', 'Resistance_Pattern', 'AMI_Concl', 'AMP_Concl',
        	'ATM_Concl', 'AUG_Concl', 'AXO_Concl', 'AZM_Concl', 'CAZ_Concl', 'CCV_Concl', 'CEP_Concl',
        	'CEQ_Concl', 'CHL_Concl', 'CIP_Concl', 'CLI_Concl', 'COT_Concl', 'CTC_Concl', 'CTX_Concl',
        	'ERY_Concl', 'FEP_Concl', 'FFN_Concl', 'FIS_Concl', 'FOX_Concl', 'GEN_Concl', 'IMI_Concl',
        	'KAN_Concl', 'NAL_Concl', 'PTZ_Concl', 'SMX_Concl', 'STR_Concl', 'TEL_Concl', 'TET_Concl',
        	'TIO_Concl' in narms_year_age.columns) and len(narms_year_age.columns) == 33:
            self.test_result_2 = True
        else:
            self.test_result_2 = False
        assert (self.test_result_1 & self.test_result_2) == True

    def test_merge_processor():
    	""" Check if the merged dataframe consists of the subset of columns from
        other dataframe and check the length of the columns."""
        if ('subject_id', 'hadm_id', 'Code', 'Descriptor', 'icd9_code', 'long_title',
            'admission_type', 'diagnosis', 'insurance', 'language', 'religion',
            'marital_status', 'ethnicity', 'gender', 'expire_flag', 'age', 'age_death',
            'age_group', 'admit_year', 'admit_new', 'disch_new', 'description', 'drug_type',
            'drug', 'formulary_drug_cd' in merge_all_salmonella.columns) and
            len(merge_all_salmonella.columns) == 25:
            self.test_result_1 = True
        else:
            self.test_result_1 = False

        assert test_result == True

if __name__ == '__main__':
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
    print(merge_all_salmonella.info())

    unittest.main()
