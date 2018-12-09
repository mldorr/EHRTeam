import pdfkit
import pandas as pd
import query as qu

from fpdf import FPDF, HTMLMixin

class HTML2PDF(FPDF, HTMLMixin):
    pass

def html_maker(list_content, narms):
    list_name = ['subject_id', 'hadm_id', 'Code', 'Descriptor',	'icd9_code',
    'long_title', 'admission_type',	'diagnosis', 'insurance', 'language', 'religion',
    'marital_status', 'ethnicity', 	'gender', 'expire_flag', 'age',	'age_death',
    'age_group', 'admit_year', 'admit_new', 'disch_new', 'description',
    'drug_type', 'drug', 'formulary_drug_cd']

    list_narms = ['Data_Year', 'Age_Group', 'Specimen_ID', 'Resistance_Pattern', 'AMI_Concl',
     'AMP_Concl', 'ATM_Concl', 'AUG_Concl', 'AXO_Concl', 'AZM_Concl', 'CAZ_Concl',
     'CCV_Concl', 'CEP_Concl', 'CEQ_Concl', 'CHL_Concl', 'CIP_Concl', 'CLI_Concl',
     'COT_Concl', 'CTC_Concl', 'CTX_Concl', 'ERY_Concl', 'FEP_Concl', 'FFN_Concl',
     'FIS_Concl', 'FOX_Concl', 'GEN_Concl', 'IMI_Concl', 'KAN_Concl', 'NAL_Concl',
     'PTZ_Concl', 'SMX_Concl', 'STR_Concl', 'TEL_Concl', 'TET_Concl', 'TIO_Concl']

    variable = {}
    table_narms = {}

    for count in range(0, len(list_name)):
        b = list_content[count]
        if(isinstance(b,list)):
            if (len(b) > 5):
                list_content[count] = list_content[count][:1]
        list_content[count] = str(list_content[count])
        variable[list_name[count]] = list_content[count]
    #print('line24' + variable['language'])
    for count in range(0, len(list_narms)):
        #narms[count] = str(narms[count])
        table_narms[list_narms[count]] = str(narms.iloc[0][count])
    for x in table_narms:
        print(x,table_narms[x])
    #<img src="eCRx_logo.png" alt="eCRx Logo" style="float:left;width:100px;height:83px;">
    html = '''
    <hr>
    <h1 align="center">Patient Case Report Form</h1>
    <hr>

    <div class="bordered" style="float: left; width: 48%;">
    <h3>Patient Information</h3>
    <p>
    <b>Subject ID:</b> ''' + variable['subject_id'] + '''<br>
    <b>Hospital Visit ID:</b> ''' + variable['hadm_id'] + '''<br>
    <b>Age:</b> ''' + variable['age'] + '''<br>
    <b>Deceased:</b>  ''' + variable['expire_flag'] + '''<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<b>Age at Death:</b> ''' + variable['age_death'] + '''<br>
    <b>Gender:</b> ''' + variable['gender'] + '''<br>
    <b>Ethnicity:</b> ''' + variable['ethnicity'] + '''<br>
    <b>Primary Language:</b> ''' + variable['language'] + '''<br>
    <b>Marital Status:</b> ''' + variable['marital_status'] + '''<br>
    <b>Religion:</b> ''' + variable['religion'] + '''<br>
    <b>Insurance:</b> ''' + variable['insurance'] + '''<br>
    </p>
    </div>
    <div class="bordered" style="float: right; width: 50%;">
    <p>
    <h3>Disease Information</h3>
    <b>Condition Diagnosis Code:</b> ''' + variable['Code'] + '''<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<b>Descriptor:</b> ''' + variable['Descriptor'] + '''<br>
    <b>All Diagnoses:</b> ''' + variable['long_title'] + '''<br>
    <b>Hospital Admission Type:</b>''' + variable['admission_type'] + ''' <br>
    <b>Admission Date:</b> ''' + variable['admit_new'] + '''<br>
    <b>Discharge Date:</b> ''' + variable['disch_new'] + '''<br>
    <h3>Prescription Information</h3>
    <b>Medications:</b> ''' + variable['drug'] + '''<br>
    </div>
    <br>
    <div class="bordered2" style="float: left; width: 100%;">
    <p>
    <h3>NARMS Data</h3>
    <br>
    <b>List</b><br>
    AMI	Amikacin : ''' + table_narms['AMI_Concl'] + '''<br>
    AMP Ampicillin : ''' + table_narms['AMP_Concl'] + '''<br>
    ATM	Aztreonam : ''' + table_narms['ATM_Concl'] + '''<br>
    AUG	Amoxicillin-clavulanic acid: ''' + table_narms['AUG_Concl'] + '''<br>
    AXO	Ceftriaxone: ''' + table_narms['AXO_Concl'] + '''<br>
    AZM	Azithromycin: ''' + table_narms['AZM_Concl'] + '''<br>
    CAZ	Ceftazidime: ''' + table_narms['CAZ_Concl'] + '''<br>
    CCV	Ceftazidime-clavulanic acid: ''' + table_narms['CCV_Concl'] + '''<br>
    CEP	Cephalothin: ''' + table_narms['CEP_Concl'] + '''<br>
    CEQ	Cefquinome: ''' + table_narms['CEQ_Concl'] + '''<br>
    CHL	Chloramphenicol: ''' + table_narms['CHL_Concl'] + '''<br>
    CIP	Ciprofloxacin: ''' + table_narms['CIP_Concl'] + '''<br>
    CLI	Clindamycin: ''' + table_narms['CLI_Concl'] + '''<br>
    COT	Trimethoprim-sulfamethoxazole: ''' + table_narms['COT_Concl'] + '''<br>
    CTC	Cefotaxime-clavulanic acid: ''' + table_narms['CTC_Concl'] + '''<br>
    CTX	Cefotaxime: ''' + table_narms['CTX_Concl'] + '''<br>
    ERY	Erythromycin: ''' + table_narms['ERY_Concl'] + '''<br>
    FEP	Cefepime: ''' + table_narms['FEP_Concl'] + '''<br>
    FFN	Florfenicol: ''' + table_narms['FFN_Concl'] + '''<br>
    FIS	Sulfisoxazole: ''' + table_narms['FIS_Concl'] + '''<br>
    FOX	Cefoxitin: ''' + table_narms['FOX_Concl'] + '''<br>
    GEN	Gentamicin: ''' + table_narms['GEN_Concl'] + '''<br>
    IMI	Imipenem: ''' + table_narms['IMI_Concl'] + '''<br>
    KAN	Kanamycin: ''' + table_narms['KAN_Concl'] + '''<br>
    NAL	Naladixic acid: ''' + table_narms['NAL_Concl'] + '''<br>
    PTZ	Piperacillin-tazobactam: ''' + table_narms['PTZ_Concl'] + '''<br>
    SMX	Sulfamethoxazole: ''' + table_narms['SMX_Concl'] + '''<br>
    STR	Streptomycin: ''' + table_narms['STR_Concl'] + '''<br>
    TEL	Telithromycin: ''' + table_narms['TEL_Concl'] + '''<br>
    TIO	Ceftiofur: ''' + table_narms['TIO_Concl'] + '''<br>
    TET	Tetracycline: ''' + table_narms['TET_Concl'] + '''<br>

    </p>
    </div>
    <img src="eCRx_logo.png" alt="eCRx Logo" style="float:left;width:10px;height:8.3px;">
    '''
    #  line 123  MER	Meropenem: ''' + table_narms['MER_Concl'] + '''<br>
    #fileb = open('html_out.txt','w')
    #fileb.write(html)
    print(table_narms)
    return html

def pdfgenerator(df, df2):
    data_row = df.iloc[0]
    list = (data_row.tolist())
    html = html_maker(list, df2)
    pdf = HTML2PDF()
    pdf.add_page()
    pdf.write_html(html)
    pdf.output('html2pdf.pdf')

def get_report(subject_id, year, age):
    df=pd.read_csv('test_file.csv')
    list_tolist = reversed(['hadm_id', 'Code', 'Descriptor',	'icd9_code',
    'long_title', 'admission_type',	'diagnosis', 'insurance', 'language', 'religion',
    'marital_status', 'ethnicity', 	'gender', 'expire_flag', 'age',	'age_death',
    'age_group', 'admit_year', 'admit_new', 'disch_new', 'description',
    'drug_type', 'drug', 'formulary_drug_cd'])

    table = qu.querySingle(df, 'subject_id', subject_id, ["subject_id"], list_tolist, ["subject_id"])

    for column in list_tolist:
        if column not in list(table.columns.values):
            table[column] = 'Nah'
    #print(table.columns.values)


    table_narms = qu.narms_query("narm's processed.csv", year,  age)


    pdfgenerator(table,table_narms)

if __name__ == '__main__':
    get_report(61, 1996, '0-4')
