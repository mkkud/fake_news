# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:17:28 2020

@author: Marek
"""

import pandas as pd


filepath = 'C:\\dane\\scrape\\scrapowane\\koronawirus_pl_2020-01-01_2020-01-31.csv'

data= pd.read_csv(filepath, index_col = [0])

print(data.info())


#dealing with missing values
#data['Mentions'] = data['Mentions'].fillna(value = 'none')
#data['Hashtags'] = data['Hashtags'].fillna(value = 'none')
data = data.drop('Geolocation', axis = 1)


print('dropped some stuff')
print(data.info())

data.to_csv('DATA_CLEAN.csv')
print('exported')