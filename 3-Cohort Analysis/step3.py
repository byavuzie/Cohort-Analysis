import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv("C:/Users/90546/OneDrive/Masaüstü/cohorts.csv")  #importing dataset 

plt.figure(figsize=(10,6)) #trend of duration time
plt.plot(data["Date"],data["Duration Day 1"],label="Duration Day 1",marker='o',color='blue')
plt.plot(data["Date"],data["Duration Day 7"],label='Duration Day 2',color='red',marker='o')

plt.ylabel("Duration Time")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.title("Trend of Duration")
plt.show()