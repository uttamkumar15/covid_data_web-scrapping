from cgitb import html
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
url = 'https://www.worldometers.info/coronavirus/'
# SENDING REQUEST TO TAKE HTML DATA
r = requests.get(url)
htmlpage = r.text

# Extracting TAble Data
soup = BeautifulSoup(htmlpage,'lxml')
get_table = soup.find('table', id = 'main_table_countries_today')
get_table_data = get_table.tbody.find_all('tr')
dic = {}
for i in range (len(get_table_data)):
    key = get_table_data[i].find_all('td')[0].string
    values = [j.string for j in get_table_data[i].find_all('td')]
    dic[key] = values
columns_name = ['country','Total Cases','New Cases','Total Deaths','New Deaths','Total Recovered','New Recovered','Active Cases','Serious Critical',"Tot Cases/1M pop",'Death/1M pop','Total Tests','Tests/1M pop','Population']

df = pd.DataFrame(dic).iloc[1:,:].T.iloc[:,:14]
df.columns = columns_name
df.replace(to_replace=[None], value=np.nan, inplace = True)
print(df.head())