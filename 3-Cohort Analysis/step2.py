import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv("C:/Users/90546/OneDrive/Masaüstü/cohorts.csv")  #importing dataset 

plt.figure(figsize=(10,6)) #trend of  new and returning users over time
plt.plot(data['Date'],data['New users'],label='New Users',color='blue',marker='o')
plt.plot(data['Date'],data['Returning users'],label='Returnin Users',color='red',marker='o')
plt.title("Trend of New and Returning Users Over Time")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Number of Users")
plt.xticks(rotation=45)
plt.show()