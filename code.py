# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(index=str,columns={"Total":"Total_Medals"},inplace=True)
print(data.head(10))


# --------------
#Code starts here



data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer',np.where(data['Total_Summer'] < data['Total_Winter'],'Winter',np.where(data['Total_Summer'] == data['Total_Winter'],'Both',np.nan)))
#print(data.head(10)) 
better_event = data['Better_Event'].value_counts().sort_values(ascending=False).idxmax()
print(better_event)





# --------------
#Code starts here



top_countries = pd.DataFrame(data,columns=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])
#top_countries =
top_countries.drop(top_countries.tail(1).index,inplace=True)
#print(top_countries)

def top_ten(frame,col_name):
    country_list=[]
    top_10 = frame.nlargest(10,col_name)
    country_list = top_10['Country_Name']
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer').tolist()
top_10_winter = top_ten(top_countries,'Total_Winter').tolist()
top_10 = top_ten(top_countries,'Total_Medals').tolist()
print(top_10_summer)
print(top_10_winter)
print(top_10)
#common = []
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)




# --------------
#Code starts here



summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot.bar(x='Country_Name',y='Total_Summer')
plt.show()

summer_df.plot.bar(x='Country_Name',y='Total_Winter')
plt.show()

summer_df.plot.bar(x='Country_Name',y='Total_Medals')
plt.show()


# --------------
#Code starts here


summer_df = summer_df.reset_index()
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
#print(summer_df.head())
summer_max_ratio_id = summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = summer_df['Golden_Ratio'].loc[summer_max_ratio_id]
print(summer_max_ratio)
summer_country_gold = summer_df['Country_Name'].loc[summer_max_ratio_id]
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio_id = winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = winter_df['Golden_Ratio'].loc[winter_max_ratio_id]
print(winter_max_ratio)
winter_country_gold = winter_df['Country_Name'].loc[winter_max_ratio_id]
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio_id = top_df['Golden_Ratio'].idxmax()
top_max_ratio = top_df['Golden_Ratio'].loc[top_max_ratio_id]
print(top_max_ratio)
top_country_gold = top_df['Country_Name'].loc[top_max_ratio_id]
print(top_country_gold)



# --------------
#Code starts here
data_1 = data[:-1]


data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1

most_points_id = data_1['Total_Points'].idxmax()

most_points = data_1['Total_Points'].loc[most_points_id]
best_country = data_1['Country_Name'].loc[most_points_id]

print(most_points)
print(best_country)



# --------------
#Code starts here
best = data.loc[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


