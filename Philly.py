import requests
import shutil
import urllib
import json
import os
import io
import re
import csv
import pandas as pd
import datetime
from datetime import datetime
import numpy as np

death = pd.read_csv('deathCase.csv')
case = pd.read_csv('countryCase.csv')
death['County'] = death['County'].str.upper()

#cdc_db.columns = [['Country Short Name','Province State Name', 'County Name', 'Report Date', 'People Positive Cases Count', 'People Death Count']]
death = death.drop(['2County Population 1', 'Rate'],axis=1)
case = case.drop(['PersonsWithNegativePCR','Probable','Confirmed','Region'],axis=1)

case.columns = ['County','Total Cases']
death.columns = ['County','Total Cases']
#death['County'] = death['County'].str.upper()
death_case = pd.concat([death, case]).reset_index(drop=True)
death_case.query('County in ("BUCKS","CHESTER","MONTGOMERY","PHILADELPHIA","DELAWARE")', inplace=True)
death_case = death_case.groupby("County", as_index=False)['Total Cases'].sum().rename(columns={'Total Cases':'Total Cases'})

today = datetime.now()
todaydate = today.date()

death_case.insert(1,'Report Date',todaydate,True)
death_case.insert(0,'Province State Name','Greater Philadelphia',True)
death_case.insert(0,'Country Short Name','Greater Philadelphia',True)
death = [0, 0, 0, 0, 0]
death_case['Deaths'] = death

death_case = death_case[death_case['Report Date'] != todaydate.isoformat()]
death_case.columns = ['Country Short Name','Province State Name', 'County Name', 'Report Date', 'People Positive Cases Count', 'People Death Count']

#death_case['People Positive Cases Count'] = death_case['People Positive Cases Count'].sum(axis=1)
#gp = death_case.sum('Country Short Name'='Greater Philadelphia')
Total = death_case['People Positive Cases Count'].sum()

Total = Total.DataFrame()
print(Total)


print(death_case)
#print(death)


print()

