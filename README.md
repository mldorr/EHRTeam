![logo](eCRx_logo.png)  
  
# EHR Team - eCRx
## *Electronic Case Reporting with Integrated Antibiotic Resistance Flagging*  
**Team Members:** Maggie Dorr, Hao "Chris" Fang, Elaine Limqueco, Yiliang "Spike" Ma, B. Kevin Ramamada  
  
### Brief Description  
This project uses MIMIC III data to generate a mock electronic case report (eCR) system which integrates the CDC's National Antimicrobial Resistance Monitoring System (NARMS) data to flag patients on medications associated with recent antimicrobial resistance in their region and age group.  
  
### License  
eCRx is shared under the GNU General Public License V3 to encourage awarenesss of recent antibiotic resistance patterns during patient treatment or prescription of medication, to promote the use and development of electronic health records/reports, and to assisst in public health research and policy development.

    Copyright (C) <2018>  <Maggie Dorr, Hao "Chris" Fang, Elaine Limqueco, Yiliang "Spike" Ma, B. Kevin Ramamada  >

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any
    later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    The eCRx team can be contacted: mldorr@uw.edu
 
For more details, please see LICENSE.TXT

  
### Organization  
Directory Structure:   

    License.py  
    README.py  
    setup.py  
    eCRx_logo.pnp  
    Data  
&nbsp;&nbsp;&nbsp;&nbsp;IsolateData.csv  
&nbsp;&nbsp;&nbsp;&nbsp;mimic_drgcodes.csv  
&nbsp;&nbsp;&nbsp;&nbsp;mimic_admissions.csv  
&nbsp;&nbsp;&nbsp;&nbsp;        mimic_procedures_icd.csv  
&nbsp;&nbsp;&nbsp;&nbsp;        mimic_d_diagnoses_icd.csv  
        narm's processed.csv  
        mimic_d_procedures_icd.csv  
        salmonellaRCTC.csv  
        mimic_diagnoses_icd.csv  
    Docs  
        ComponentSpec.md  
        Final Presentation.pptx	 
        FunctionalSpec.md  
    EHRTeam  
        MainWindow.py    
        QtUI_rev.py  
        database_build.py  
        output_pdf.py  
        output_pdf_test.py
        query.py  
        sql_import.py  
        test_query.py  
        test_MainWindow.py  
    Examples  
        

### Installation  
To install eCRx:   
1. Download or clone the repository  
2. Download mimic_prescriptions (https://drive.google.com/open?id=1jKu6Qdi6weqeUJb6-RcUjY1h_YH3mSe4) and add to Data folder  
3. Run setup.py  
  
*Created for CSE 583 at the University of Washington*
