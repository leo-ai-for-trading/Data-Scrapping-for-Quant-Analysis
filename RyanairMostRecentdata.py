import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://investor.ryanair.com/traffic/'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

test = soup.find('table',class_ = 'tablepress tablepress-id-87')
m = []
pass_FY21 = []
pass_FY22 = []
ch = []
for months in test.find_all('tbody'):
    rows = months.find_all('tr') #tr is the row
    #print(rows)
    for row in rows:
        mese = row.find('td',class_='column-1').text
        passengers_fy21 = row.find('td',class_='column-2').text
        passengers_fy22 = row.find('td',class_='column-3').text
        change = row.find('td',class_='column-4').text
        m += [mese]
        pass_FY21 += [passengers_fy21]
        pass_FY22 += [passengers_fy22]
        ch += [change]
        
        #print(mese,passengers_fy21,passengers_fy22,change)


list_ = [m,pass_FY21,pass_FY22,ch]
df = pd.DataFrame(list_).transpose()
df.columns = ['Months','Passengers_2021','E_passengers_2022','E_change']
df.set_index('Months',inplace=True)
df['Passengers_2021'] = df['Passengers_2021'].str.replace('m', '')
df['Passengers_2021'] = df['Passengers_2021'].astype(float)
df['E_passengers_2022'] = df['E_passengers_2022'].str.replace('m', '')
df['E_passengers_2022'] = df['E_passengers_2022'].astype(float)

print('Data expressed in mln',df)
