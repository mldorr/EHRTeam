#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:24:24 2018

@author: haofang
"""

from setuptools import setup, find_packages
from os import path

from io import open

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

long_description="""
Public Health Researchers will be using the system to track and study antibiotic resistance patterns and 
treatment strategies. These users will be very familiar with EHR and eCR. They may have variable levels of 
familiarity with coding, from completely lacking coding skills to being bioinformatics experts. We would expect 
these users at minimum to input bacterial strains or antibiotics to the database to generate case reports in 
dpf format. This information would be used in public health research to identify and study instances of 
antibiotic resistance.
"""
setup(
    name='EHR',  # Required
    version='1.0.0',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/mldorr/EHRTeam',  # Optional
    author='Maggie Dorr, Hao Fang, Elaine Limqueco, Yiliang Ma, B. Kevin Ramamada',  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Medical',
        'Topic :: Electrical Health Record',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
   # keywords='',  # Optional
   # Come up with a keywords

    packages=find_packages(),  # Required
    install_requires=['pandas','numpy','plotly','sqlite3','matplotlib','psycopg2'],  # Optional
    # add those requaired software that was used in this project, need to add

    package_data={  # Optional
        'EHRTeam': ['Data/*.*'],
    },


    project_urls={  # Optional
        'MIMIC III': 'https://mimic.physionet.org/community/contributing/',
        'PHIN VADS': 'https://phinvads.cdc.gov/vads/SearchVocab.action',
        'NARMS': 'https://wwwn.cdc.gov/narmsnow/',
    },
)