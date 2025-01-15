import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv("C:/Users/90546/OneDrive/Masaüstü/cohorts.csv")  #importing dataset 
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