import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv("C:/Users/90546/OneDrive/Masaüstü/cohorts.csv")  #importing dataset 
print(data.head())

missing_data=data.isnull().sum()  #checking missing data 
print(missing_data)

data_type=data.dtypes  #checking data types for date column 
print(data_type)

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')  #changing data type of date column 

desc_data=data.describe()  #descriptive statistics of dataset
print(desc_data)
