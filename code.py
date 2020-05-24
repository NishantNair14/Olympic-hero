# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
better_event=data['Better_Event'].value_counts()
if better_event[0]>better_event[1]:
    better_event='Summer'
else:
    better_event='Winter'

print(better_event)



# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
#print(top_countries.tail(5))
top_countries=top_countries[:-1]

def top_ten(top_countries,col):
    country_list=[]
    country_list=top_countries.nlargest(10,col)['Country_Name']
    return country_list

top_10_summer=list(top_ten(top_countries,'Total_Summer'))
#print(top_10_summer)
top_10_winter=list(top_ten(top_countries,'Total_Winter'))

top_10=list(top_ten(top_countries,'Total_Medals'))

common=[]
common=list(set(top_10).intersection(top_10_winter,top_10_summer))
print(common)
    




# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

summer_df.plot.bar()
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')


# --------------
#Code starts here
summer_df['Golden_Ratio']=data['Gold_Summer']/data['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_max_ratio)
print(summer_country_gold)
winter_df['Golden_Ratio']=data['Gold_Winter']/data['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=data['Gold_Total']/data['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
data_1=data[:-1]
print(data_1)

data_1['Total_Points']=3*data_1['Gold_Total']+2*data_1['Silver_Total']+1*data_1['Bronze_Total']

most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points,best_country)


# --------------
#Code starts here

best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


