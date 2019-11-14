import pandas as pd
data=pd.read_csv('supermarkets.csv')
# print(data.head)

def Getpandas(Module_name):
    data=pd.read_csv(Module_name)
    return data['Employees'].min()

print(Getpandas('supermarkets.csv'))