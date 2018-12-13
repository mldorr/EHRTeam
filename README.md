![logo](eCRx_logo.png)  
  
# EHR Team - eCRx
## *Electronic Case Reporting with Integrated Antibiotic Resistance Flagging*  
**Team Members:** Maggie Dorr, Hao "Chris" Fang, Elaine Limqueco, Yiliang "Spike" Ma, B. Kevin Ramada  
  
### Brief Description  
This project uses MIMIC III data to generate a mock electronic case report (eCR) system which integrates the CDC's National Antimicrobial Resistance Monitoring System (NARMS) data to flag patients on medications associated with recent antimicrobial resistance in their region and age group.  
  
### License  
eCRx is shared under the GNU General Public License V3 to encourage awarenesss of recent antibiotic resistance patterns during patient treatment or prescription of medication, to promote the use and development of electronic health records/reports, and to assisst in public health research and policy development.

    Copyright (C) <2018>  <Maggie Dorr, Hao "Chris" Fang, Elaine Limqueco, Yiliang "Spike" Ma, B. Kevin Ramada  >

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
 
    Data  
        IsolateData.csv
        mimic_drgcodes.csv  
        mimic_admissions.csv  
        mimic_procedures_icd.csv  
        mimic_d_diagnoses_icd.csv  
        narms_processed.csv  
        mimic_d_procedures_icd.csv  
        salmonellaRCTC.csv  
        mimic_diagnoses_icd.csv  
    Docs  
        ComponentSpec.md  
        FunctionalSpec.md  
        final_presentation.pdf  
        tech_review.pdf   
    EHRTeam  
        .pylintrc  
        __init__.py  
        database_build.py  
        eCRx_logo_small.png  
        main_window.py  
        output_pdf.py  
        query.py  
        report_ui.py  
        sql_import.py  
        test_database_build.py  
        test_main_window.py  
        test_output_pdf.py  
        test_query.py  
        test_report_UI.py  
    Example  
        example.pdf
        patients.txt      
    .gitignore  
    LICENSE.md  
    README.md  
    eCRx_logo.png  
    environment.yml  
    requirements.txt  
    setup.py      

### Installation  
To install eCRx:   
1. Download or clone the repository  
2. Download mimic_prescriptions (https://drive.google.com/open?id=1jKu6Qdi6weqeUJb6-RcUjY1h_YH3mSe4) and add to Data folder  
3. Create new environment by running `environment.yml`  
4. Navigate to EHRTeam subfolder
5. Activate the new installed environment
6. Enter `python main_window.py` in the command line  
7. Enter patient information from `EHRTeam/Examples/patients.txt` 
8. Watch the magic happen    
  
*Created for CSE 583 at the University of Washington*
