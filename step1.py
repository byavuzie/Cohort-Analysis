import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
data=pd.read_csv("C:/Users/90546/OneDrive/Masaüstü/cohorts.csv")  #importing dataset 
print(data.head())

missing_data=data.isnull().sum()  #checking missing data 
print(missing_data)

data_type=data.dtypes  #checking data types for date column 
print(data_type)

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')  #changing data type of date column 

desc_data=data.describe()  #descriptive statistics of dataset
print(desc_data)

plt.figure(figsize=(10,6)) #trend of  new and returning users over time
plt.plot(data['Date'],data['New users'],label='New Users',color='blue',marker='o')
plt.plot(data['Date'],data['Returning users'],label='Returnin Users',color='red',marker='o')
plt.title("Trend of New and Returning Users Over Time")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Number of Users")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,6)) #trend of duration time
plt.plot(data["Date"],data["Duration Day 1"],label="Duration Day 1",marker='o',color='blue')
plt.plot(data["Date"],data["Duration Day 7"],label='Duration Day 2',color='red',marker='o')
plt.ylabel("Duration Time")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.title("Trend of Duration")
plt.show()

data['Date']=pd.to_datetime(data['Date']) #changing date format 

data['Week']=data['Date'].dt.isocalendar().week 
weekly_avg=data.groupby('Week').agg({
    'New users':'mean',
    'Returning users':'mean',
    'Duration Day 1':'mean',
    'Duration Day 7':'mean'
}).reset_index()
print(weekly_avg)

plt.figure(figsize=(10,6))
plt.plot(weekly_avg['Week'],weekly_avg['New users'],color='blue',marker='o',label='New Users')
plt.plot(weekly_avg['Week'],weekly_avg['Returning users'],color='red',marker='o',label='Returning User')
plt.title("Weekly Average of New and Return Users")
plt.xlabel('Weeks')
plt.xticks(rotation=45)
plt.ylabel('Average Number of Users')
plt.legend()
plt.show()

data['Week']=data['Date'].dt.isocalendar().week 
weekly_avg=data.groupby('Week').agg({
    'New users':'mean',
    'Returning users':'mean',
    'Duration Day 1':'mean',
    'Duration Day 7':'mean'
}).reset_index()
cohort_matrix = weekly_avg.set_index('Week')
plt.figure(figsize=(12, 8))

sns.heatmap(cohort_matrix, annot=True, cmap='coolwarm', fmt=".1f")
plt.title('Cohort Matrix of Weekly Averages')
plt.ylabel('Week of the Year')
plt.show()