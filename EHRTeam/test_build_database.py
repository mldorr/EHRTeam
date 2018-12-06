from build_database import import_csv, preprocess_admission, merge_dataframe

admission = preprocess_admission()
diagnoses_icd, d_diagnoses_icd, admissions, drgcodes, procedures_icd, d_procedures_icd, salmonellaTC = import_csv()

def test_admit_group_year():
    """ Check if the year is in the range of 2001 - 2012."""
    year_subset = admission['admit_new'].dt.year
    if (year_subset < 2001).any() and (year_subset > 2012).any():
        test_result = False
    else:
    	test_result = True
    assert test_result == True


def test_disch_group_year():
    """ Check if the year is in the range of 2001 - 2012."""
    year_subset = admission['disch_new'].dt.year
    if (year_subset < 2001).any() and (year_subset > 2012).any():
        test_result = False
    else:
    	test_result = True
    assert test_result == True


def test_check_admit_columns():
	""" Check if the 'admit_year','admit_month','admit_day' columns are deleted."""
	if ('admit_year' in admission.columns) or ('admit_month' in admission.columns) or ('admit_day' in admission.columns):
		test_result = False
	else:
		test_result = True
	assert test_result == True


def test_check_disch_columns():
	""" Check if the 'disch_year','disch_month','disch_day' columns are deleted."""
	admission = preprocess_admission()
	if ('disch_year' in admission.columns) or ('disch_month' in admission.columns) or ('disch_day' in admission.columns):
		test_result = False
	else:
		test_result = True
	assert test_result == True


def test_merge_dataframe():
	""" Check if the merged dataframe consists of the subset of columns from other dataframe and check the length of the columns."""
	test_result = True
	final_dataframe = merge_dataframe(admission)
	diagnoses_icd_column = diagnoses_icd.drop(columns=['Unnamed: 0']).columns
	d_diagnoses_icd_column = d_diagnoses_icd.drop(columns=['Unnamed: 0', 'icd9_code']).columns
	salmonellaICD_column = salmonellaTC.drop(columns='CodeSystem').columns
	admission_column = admission.drop(columns=['Unnamed: 0', 'subject_id', 'hadm_id']).columns
	drgcodes_column = drgcodes.drop(columns=['Unnamed: 0', 'subject_id', 'hadm_id']).columns
	
	for column in diagnoses_icd_column:
		if column not in final_dataframe.columns:
			test_result = False

	for column in d_diagnoses_icd_column:
		if column not in final_dataframe.columns:
			test_result = False

	for column in salmonellaICD_column:
		if column not in final_dataframe.columns:
			test_result = False

	for column in admission_column:
		if column not in final_dataframe.columns:
			test_result = False

	for column in drgcodes_column:
		if column not in final_dataframe.columns:
			test_result = False

	if len(final_dataframe.columns) != (len(diagnoses_icd_column) + len(d_diagnoses_icd_column) + len(salmonellaICD_column) + len(admission_column) + len(drgcodes_column)):
		test_result = False

	assert test_result == True