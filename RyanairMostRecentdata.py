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
df.columns = ['mese','passeggeri_2021','previsione_passeggeri_2022','cambio_previsto']
df.set_index('mese',inplace=True)
df['passeggeri_2021'] = df['passeggeri_2021'].str.replace(r'\D', '').astype(int)
df['previsione_passeggeri_2022'] = df['previsione_passeggeri_2022'].str.replace(r'\D', '').astype(int)
#df['cambio_previsto'] = df['cambio_previsto'].str.rstrip('%')

print(df)
