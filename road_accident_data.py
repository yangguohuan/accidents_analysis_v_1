import matplotlib.pyplot as plt
import pandas as pd

'''
数据处理
'''

df = pd.read_excel('RoadAccidentData.xlsx')
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.duplicated().sum())
#print(df.isnull().sum())
columns_to_fill = ['Carriageway_Hazards','Road_Surface_Conditions','Road_Type','Time','Weather_Conditions']
df[columns_to_fill] = df[columns_to_fill].fillna('null')
df = df.drop_duplicates()

series = df['Junction_Detail'].value_counts()
series_index = series.index.tolist()
series_values = series.values.tolist()


'''
生成图表
'''
fig, ax = plt.subplots(2, 1)
fig.suptitle('Junction Details Analysis of Road Accidents', fontsize=16)

ax[0].bar(series_index, series_values)
ax[0].set_xlabel('accidents type')
ax[0].set_ylabel('counts')
ax[0].tick_params(axis='x', rotation=-45)
ax[0].set_title('Bar Chart of Accident Types')

ax[1].pie(series_values, labels=series_index, autopct='%1.1f%%')
ax[1].set_title('Pie Chart of Accident Types')

plt.tight_layout()
plt.show()