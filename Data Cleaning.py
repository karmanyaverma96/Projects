# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:00:30 2021

@author: Admin
"""
import pandas as pd

# preparing data
traveler = pd.DataFrame({'user_id': [136, 284, 101, 529, 800, 823], 'age':
[None, 38, 30, 43, 49, 28], 'name': ["Ann", "Ben", "Tom", "Bianca", "Caroline",
"Kate"]})

travel = pd.DataFrame({'user_id': [101, 284, 136, 800, 101, 800, 823, 529, 284],
'date_of_journey': ['2018-01-16', '2017-07-13','2019-10-10','2018/03/20',
'2019-12-24', '2017-10-17','2016/11/02',
'2019/09/14', '2019-08-07'],'duration': [10, 10,7,13,7,11,14, 8, 12],
'destination': ["New Zeland", "australia", "Australia", "New_Zealand",
"Australia/","Australia", "New Zealand", "Australia", "New_zealand"], 'cost':
[None, 2325.0, 1760.0, 2740.0, 4000.0, 2475.0, 3140.0, 1840.0, 2910.0],
'currency': [None, 'EUR', 'GBP', 'GBP', 'GBP','EUR', 'GBP', 'GBP', 'GBP']})

traveler.to_csv("traveler.csv", index=False)
travel.to_csv("travel.csv", index=False)


# 1. Merge two csv files.

traveler = pd.read_csv("traveler.csv")
travel = pd.read_csv("travel.csv")

data = pd.merge(travel, traveler, on='user_id')
data

# 2. Make data consistent  .

# 2.a) as there are several datetime formats.


data.date_of_journey = pd.to_datetime(data.date_of_journey,
infer_datetime_format=True)
data


# 2.b) cost is given in two currencies, hence change them to GBP.

data.loc[data.currency == 'EUR', ['cost']] = data.cost*0.8
data.currency.replace("EUR", "GBP", inplace=True)
data

# 2.c) the destination column contains more unique values than expected. It should include two values and that’s why we need to fix that by changing every string respectively to new_zealand or to australia.


data.destination.describe()

# get all compromised categories and unify them.


categories = data.drop_duplicates()
print(categories)


data.destination.loc[data.destination.str.lower().str.startswith('n', na=False)] = "new_zealand"
data.destination.loc[data.destination.str.lower().str.startswith('a', na=False)] = "australia"
data


# 3. dropping currency and name column since its not needed in the analysis.


data = data.drop(['currency','name'], axis=1)
data



# 4. Missing values

data.isna()

    #  fill missing values of cost with mean travel cost for new zealand
    #  fill age with mean value of age column
    
values = {'cost': data.cost.where(data.destination=='new_zealand').mean(), 'age':
round(data.age.mean())}
print('values:',values)
data = data.fillna(value=values, limit=1)
data


# 5. map the destination column values to {‘new_zealand’: 0, ‘australia’: 1} which is more readable for a machine than strings.


data.destination.replace(('new_zealand','australia'), (0,1), inplace=True)
data 


# 6. Identify outliers using scatter plot and boxplot.


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams['figure.figsize'] = [10,7]

x = data.duration
y = data.cost
z = data.destination

fig, ax = plt.subplots()

scatter = ax.scatter(x, y , c=z, s= np.pi*100, marker='o', alpha=0.5)

# produce a legend with unique colors from the scatter

legend = ax.legend(*scatter.legend_elements(), loc=1, title='Destination')

ax.add_artist(legend)
legend.get_texts()[0].set_text('new_zealand')
legend.get_texts()[1].set_text('australia')

plt.title('Travel costs vs travel duration for Australia and New Zealand')
plt.xlabel('travel duration')
plt.ylabel('travel costs')
plt.show()


boxplot = data.boxplot(column=['cost'], by=['destination'])
plt.xticks([1, 2], ['new_zealand', 'australia']);

data = data.drop(data.index[data.cost == data.cost.max()], axis=0)
data


