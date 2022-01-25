import pandas as pd
"""
Data grouping adalah menggrupkan sebuah data dalam satu kireteria tertentu
"""


#loading data
data = pd.read_csv("D:/TeguhPermana_data/Data_Grouping/athlete_events.csv")
print(data.head(10))

#pengelompokan data
data_grouped=data.groupby(["Sport","Name"])["Age","Height","Weight"].mean()
print(data_grouped.head(10))