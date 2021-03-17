
import pandas as pd
import numpy as np
import statsmodels.api as sm
import datettime 

starttime = datetime.datetime.now()


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\2021 0316.xlsx', sheet_name = 'Transfer')

table = table.iloc[6:, 2: ]
table.columns = ['ID', 'CountryID', 'PeriodID', 'Country', 'Period', 'value', 'Choose', 'CDD', 'HDD', 'Year', 'CMA', 'Dev%']
table[['CountryID']] = table[['CountryID']].astype('float')
table[['value']] = table[['value']].astype('float')
table[['CDD']] = table[['CDD']].astype('float')
table[['HDD']] = table[['HDD']].astype('float')
table[['Choose']] = table[['Choose']].astype('float')
table[['Year']] = table[['Year']].astype('float')
table[['Dev%']] = table[['Dev%']].astype('float')

table = table.dropna(subset=['value'])
#########
### loop~ ^_^

## use value as y

# before running loop, run below
output = pd.DataFrame(columns = ['CountryID', 'Method', 'R2', 'Constant', 'CoefCDD', 'CoefHDD', 'Constant-t', 'CoefCDD-t', 'CoefHDD-t'])

# all year round
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]

 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['value']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["all year"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output = output.append(new_row2, ignore_index=True, sort=False)

# manual choose
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]
 tablei = tablei.drop(tablei[tablei.Choose == 0].index)
 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['value']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["manual choose"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output = output.append(new_row2, ignore_index=True, sort=False)

# recent 3 years, drop year < 2018
# delete CountryID = 51: Libya; 
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]
 tablei = tablei.drop(tablei[tablei.Year < 2018].index)
 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['value']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["3-year"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output = output.append(new_row2, ignore_index=True, sort=False)
 
# recent 2 years, drop year < 2019
# delete CountryID = 51: Libya; 
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]
 tablei = tablei.drop(tablei[tablei.Year < 2018].index)
 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['value']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["2-year"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output = output.append(new_row2, ignore_index=True, sort=False)
 
###########
 output.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality - Global\\Regression Results - value as y.csv',index=None)


## use dev% as y

# before running loop, run below
output2 = pd.DataFrame(columns = ['CountryID', 'Method', 'R2', 'Constant', 'CoefCDD', 'CoefHDD', 'Constant-t', 'CoefCDD-t', 'CoefHDD-t'])

# all year round
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]

 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['Dev%']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["all year"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output2 = output2.append(new_row2, ignore_index=True, sort=False)

# manual choose
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]
 tablei = tablei.drop(tablei[tablei.Choose == 0].index)
 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['Dev%']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["manual choose"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output2 = output2.append(new_row2, ignore_index=True, sort=False)

# recent 3 years, drop year < 2018
# delete CountryID = 51: Libya; 
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]
 tablei = tablei.drop(tablei[tablei.Year < 2018].index)
 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['Dev%']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["3-year"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output2 = output2.append(new_row2, ignore_index=True, sort=False)
 
# recent 2 years, drop year < 2019
# delete CountryID = 51: Libya; 
for i in [1, 2, 9, 13, 15, 17, 18, 20, 24, 25, 26, 29, 30, 31, 32, 33, 35, 36, 37, \
          39, 44, 45, 49, 50, 52, 53, 58, 59, 61, 62, 63, 64, 68, 69, 70, 71, \
          72, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 90, ]:
 tablei = table[table['CountryID'] == i]
 tablei = tablei.drop(tablei[tablei.Year < 2018].index)
 x = sm.add_constant(tablei.iloc[:,7:9]) #生成自变量
 y = tablei['Dev%']
 model = sm.OLS(y, x, missing='drop')
 results = model.fit()
 results.summary()
 values = pd.DataFrame(results.params)
 values.columns = ['coef']
 t_stat = pd.DataFrame(results.tvalues)
 t_stat.columns = ['t-statistic']

 r2 = results.rsquared 
 new_row = {'CountryID': [i], 'Method':["2-year"], 'R2': [r2], 'Constant': [values.iloc[0,0]], 'CoefCDD': [values.iloc[1,0]], 'CoefHDD': [values.iloc[2,0]], \
            'Constant-t': [t_stat.iloc[0,0]], 'CoefCDD-t': [t_stat.iloc[1,0]], 'CoefHDD-t': [t_stat.iloc[2,0]],}
 
 new_row2 = pd.DataFrame(new_row)
 output2 = output2.append(new_row2, ignore_index=True, sort=False)
 
###########
 output2.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality - Global\\Regression Results - dev% as y.csv',index=None)

          
          endtime = datetime.datetime.now()
print("Congradulations! Finished") 
print("duraion", endtime - starttime)

