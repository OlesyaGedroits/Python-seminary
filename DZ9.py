# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population)
# и сохранить ее в переменную avg.
# import pandas as pd
# file='california_housing_train.csv'
# df=pd.read_csv(file)
# avg=df[(df['population']>0)&(df['population']<=500)]['median_house_value'].mean()
# print(avg)


# Дан файл california_housing_train.csv. Найти максимальное значение переменной "households"
# в зоне минимального значения переменной min_population и сохраните это значение в переменную max_households_in_min_population.

#'longitude','latitude','housing_median_age', 'total_rooms','total_bedrooms','population','households','median_income','median_house_value'

import pandas as pd
file='california_housing_train.csv'
df=pd.read_csv(file)

min_population=df['population'].min()

max_households_in_min_population=df['households'][(df['population']==min_population)].max()

print(max_households_in_min_population)