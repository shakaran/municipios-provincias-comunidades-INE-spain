#!/usr/bin/env python3.4
# *-* coding: utf-8 *-*

import pandas as pd

# Fetch municipalities from INE (year 2015)
data = pd.ExcelFile('http://www.ine.es/daco/daco42/codmun/codmun15/15codmun.xls')

first_sheet = data.sheet_names[0]

# Fetch first sheet and skip the first 2 rows (headers)
data_parsed = data.parse(sheetname = 0, skiprows = 1)

import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///municipalities_spain.sqlite')

data_parsed.to_sql('municipalities_spain', engine, if_exists='replace', index=True)

print 'File municipalities_spain.sqlite generated.\nTo export to SQL run: sqlite3 municipalities_spain.sqlite .dump > municipalities_spain_aux.sql'
