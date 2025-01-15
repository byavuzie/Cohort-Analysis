import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("C:/Users/90546/OneDrive/Masaüstü/cohorts.csv")  #importing dataset 
data['Date']=pd.to_datetime(data['Date']) #changing date format 

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