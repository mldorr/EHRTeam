''' a test version module for output_pdf.py'''
import unittest
import output_pdf as op
import query as qu
import pandas as pd

class UnitTests(unittest.TestCase):
    '''a class of test collection '''
    def test1(self):
        '''
        test1 is to test if the html is the same as we expect
        '''
        df1 = pd.read_csv('../Data/test_file.csv')
        list_tolist = reversed(['hadm_id', 'Code', 'Descriptor', 'icd9_code',
                                'long_title', 'admission_type',	'diagnosis', 'insurance',
                                'language', 'religion', 'marital_status', 'ethnicity',
                                'gender', 'expire_flag', 'age', 'age_death',
                                'age_group', 'admit_year', 'admit_new', 'disch_new', 'description',
                                'drug_type', 'drug', 'formulary_drug_cd'])
        table = qu.query_single(df1, 'subject_id', 61, ["subject_id"],
                               list_tolist, ["subject_id"])

        for column in list_tolist:
            if column not in list(table.columns.values):
                table[column] = 'Nah'
        table_narms = qu.narms_query("../Data/narms_processed.csv",1996, '0-4')
        data_row = table.iloc[0]
        list_tem = (data_row.tolist())
        html = op.html_maker(list_tem, table_narms)

        f = open('tem_out.csv','w')
        f.write(html)
        html_template = '''
    <hr>
    <h1 align="center">Patient Case Report Form</h1>
    <hr>

    <div class="bordered" style="float: left; width: 48%;">
    <h3>Patient Information</h3>
    <p>
    <b>Subject ID:</b> 61<br>
    <b>Hospital Visit ID:</b> 189535<br>
    <b>Age:</b> 55<br>
    <b>Deceased:</b>  Death<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<b>Age at Death:</b> 55<br>
    <b>Gender:</b> M<br>
    <b>Ethnicity:</b> WHITE<br>
    <b>Primary Language:</b> nan<br>
    <b>Marital Status:</b> MARRIED<br>
    <b>Religion:</b> CATHOLIC<br>
    <b>Insurance:</b> Private<br>
    </p>
    </div>
    <div class="bordered" style="float: right; width: 50%;">
    <p>
    <h3>Disease Information</h3>
    <b>Condition Diagnosis Code:</b> 99591<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<b>Descriptor:</b> Salmonella sepsis<br>
    <b>All Diagnoses:</b> Acidosis<br>
    <b>Hospital Admission Type:</b>EMERGENCY <br>
    <b>Admission Date:</b> 2002-01-04<br>
    <b>Discharge Date:</b> 2002-02-03<br>
    <h3>Prescription Information</h3>
    <b>Medications:</b> Amino Acids 4.25% W/ Dextrose 5% ,  Calcium Gluconate ,  Digoxin ,  Potassium Chloride ,  Potassium Chloride ,  Multivitamin IV ,  Heparin Flush PICC (100 units/ml) ,  Digoxin ,  Digoxin ,  Insulin ,  Hydrocortisone Na Succ. ,  Syringe ,  Insulin ,  Insulin ,  NS ,  Hydrocortisone Na Succ. ,  Digoxin ,  Neutra-Phos ,  Vial ,  Vial ,  Sodium Phosphate ,  Potassium Chloride ,  Hydrocortisone Na Succ. ,  Potassium Chloride ,  Daptomycin ,  NS ,  Levofloxacin ,  Potassium Chloride ,  SW ,  Potassium Chloride ,  Potassium Chloride ,  NS ,  Hydrocortisone Na Succ. ,  Vial ,  Diltiazem ,  NS ,  Potassium Chloride ,  Potassium Chloride ,  Potassium Chloride ,  Potassium Phosphate ,  SW ,  SW ,  SW ,  Spironolactone ,  Vial ,  Filgrastim ,  Potassium Chloride ,  Potassium Chloride ,  Hydrocortisone Na Succ. ,  Caspofungin<br>
    </div>
    <br>
    <div class="bordered2" style="float: left; width: 100%;">
    <p>
    <h3>NARMS Data</h3>
    <br>
    <b>List</b><br>
    AMI	Amikacin : 0<br>
    AMP Ampicillin : 2<br>
    ATM	Aztreonam : 0<br>
    AUG	Amoxicillin-clavulanic acid: 0<br>
    AXO	Ceftriaxone: 0<br>
    AZM	Azithromycin: 0<br>
    CAZ	Ceftazidime: 0<br>
    CCV	Ceftazidime-clavulanic acid: 0<br>
    CEP	Cephalothin: 0<br>
    CEQ	Cefquinome: 0<br>
    CHL	Chloramphenicol: 2<br>
    CIP	Ciprofloxacin: 0<br>
    CLI	Clindamycin: 0<br>
    COT	Trimethoprim-sulfamethoxazole: 0<br>
    CTC	Cefotaxime-clavulanic acid: 0<br>
    CTX	Cefotaxime: 0<br>
    ERY	Erythromycin: 0<br>
    FEP	Cefepime: 0<br>
    FFN	Florfenicol: 0<br>
    FIS	Sulfisoxazole: 0<br>
    FOX	Cefoxitin: 0<br>
    GEN	Gentamicin: 0<br>
    IMI	Imipenem: 0<br>
    KAN	Kanamycin: 0<br>
    NAL	Naladixic acid: 0<br>
    PTZ	Piperacillin-tazobactam: 0<br>
    SMX	Sulfamethoxazole: 2<br>
    STR	Streptomycin: 2<br>
    TEL	Telithromycin: 0<br>
    TIO	Ceftiofur: 0<br>
    TET	Tetracycline: 3<br>

    </p>
    </div>
    <img src="eCRx_logo_small.png" alt="eCRx Logo" style="float:left;width:10px;height:8.3px;">
   
    '''
        self.assertEqual(len(html), len(html_template))

    def test2(self):
        '''
        test if get_report works well
        '''
        op.get_report(61, 1941)

if __name__ == '__main__':
    unittest.main()
