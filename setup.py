
"""
Created on Sun Nov 25 22:24:24 2018

@author: haofang
"""

from io import open
from os import path
from setuptools import setup, find_packages




HERE = path.abspath(path.dirname(__file__))


with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

LONG_DESCRIPTION = """
Public Health Researchers will be using the system to track and study antibiotic resistance patterns and 
treatment strategies. These users will be very familiar with EHR and eCR. They may have variable levels of 
familiarity with coding, from completely lacking coding skills to being bioinformatics experts. We would expect 
these users at minimum to input bacterial strains or antibiotics to the database to generate case reports in 
dpf format. This information would be used in public health research to identify and study instances of 
antibiotic resistance.
"""

setup(
    name='EHR',
    version='1.0.0',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/mldorr/EHRTeam',
    author='Maggie Dorr, Hao Fang, Elaine Limqueco, Yiliang Ma, B. Kevin Ramamada',
    classifiers=[

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Medical',
        'Topic :: Electrical Health Record',


        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],


    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'plotly', 'sqlite3', 'matplotlib', 'psycopg2',
                      'PyQt5', 'QtUI_rev', 'fpdf', 'query'],

    package_data={
        'EHRTeam': ['Data/*.*'],
    },


    project_urls={
        'MIMIC III': 'https://mimic.physionet.org/community/contributing/',
        'PHIN VADS': 'https://phinvads.cdc.gov/vads/SearchVocab.action',
        'NARMS': 'https://wwwn.cdc.gov/narmsnow/',
    },
)
