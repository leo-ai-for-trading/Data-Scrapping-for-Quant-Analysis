#Another way to obtain data and convert into DataFrame
import pandas as pd


url = 'https://investor.ryanair.com/traffic/'
df = pd.read_html(url,parse_dates=True)

pss_21 = df[2]['FY21']
l_pss_21 = df[3]['FY21']
pss_20 = df[4]['FY20']
l_pss_20 = df[5]['FY20']
pss_19 = df[6]['FY19']
l_pss_19 = df[7]['FY19']
pss_18 = df[8]['FY18']
l_pss_18 = df[9]['FY18']
pss_17 = df[10]['FY17']
l_pss_17 = df[11]['FY17']
pss_16 = df[12]['FY16']   
l_pss_16 = df[13]['FY16']
pss_15 = df[14]['FY15']   
l_pss_15 = df[15]['FY15']
pss_14 = df[16]['FY14']
l_pss_14 = df[17]['FY14']
pss_13 = df[18]['FY13']
l_pss_13 = df[19]['FY13']
pss_12 = df[20]['FY12']         
l_pss_12 = df[21]['FY12']
month = df[12]['Unnamed: 0']

passengers = {'Month':month,'FY12':pss_12,'FY13':pss_13,'FY14':pss_14,'FY15':pss_15,
'FY16':pss_16,'FY17':pss_17,'FY18':pss_18,'FY19':pss_19,'FY20':pss_20,'FY21':pss_21}

load_factor = {'Load_fac12':l_pss_12,'Load_fac13':l_pss_13,'Load_fac14':l_pss_14,
'Load_fac15':l_pss_15,'Load_fac16':l_pss_16,'Load_fac17':l_pss_17,
'Load_fac18':l_pss_18,'Load_fac19':l_pss_19,'Load_fac20':l_pss_20,'Load_fac21':l_pss_21}


data = pd.DataFrame.from_dict({**passengers,**load_factor})
data.set_index('Month',inplace=True)
data['FY12'] = data['FY12'].str.replace('m', '').astype(float)
data['FY13'] = data['FY13'].str.replace('m', '').astype(float)
data['FY14'] = data['FY14'].str.replace('m', '').astype(float)
data['FY15'] = data['FY15'].str.replace('m', '').astype(float)
data['FY16'] = data['FY16'].str.replace('m', '').astype(float)
data['FY17'] = data['FY17'].str.replace('m', '').astype(float)
data['FY18'] = data['FY18'].str.replace('m', '').astype(float)
data['FY19'] = data['FY19'].str.replace('m', '').astype(float)
data['FY20'] = data['FY20'].str.replace('m', '').astype(float)
data['FY21'] = data['FY21'].str.replace('m', '').astype(float)
data['Load_fac12'] = data['Load_fac12'].str.replace('%', '').astype(float)/100
data['Load_fac13'] = data['Load_fac13'].str.replace('%', '').astype(float)/100
data['Load_fac14'] = data['Load_fac14'].str.replace('%', '').astype(float)/100 
data['Load_fac15'] = data['Load_fac15'].str.replace('%', '').astype(float)/100
data['Load_fac16'] = data['Load_fac16'].str.replace('%', '').astype(float)/100
data['Load_fac17'] = data['Load_fac17'].str.replace('%', '').astype(float)/100 
data['Load_fac18'] = data['Load_fac18'].str.replace('%', '').astype(float)/100
data['Load_fac19'] = data['Load_fac19'].str.replace('%', '').astype(float)/100
data['Load_fac20'] = data['Load_fac20'].str.replace('%', '').astype(float)/100
data['Load_fac21'] = data['Load_fac21'].replace('-', None)


print(data)
