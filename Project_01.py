# loading the all types of file in python using pandas library


import pandas as pd 
# df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
# df2 = pd.read_json('sample_Data.json')
df3 = pd.read_excel('sampleSuperstore.xlsx')
# , encoding='utf-8'
# , encoding='latin1'   
# print(df)
# print(df2)
print(df3)
#  if you data at any store data on  cloud storage 
# than use this is libray and its name is gcsfs