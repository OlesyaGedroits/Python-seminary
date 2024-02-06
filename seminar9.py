#pip install pandas
import pandas as pd
file='california_housing_train.csv'
df=pd.read_csv(file)


# print(df.dtypes)
# print(df.isnull().sum())
# df2.to_csv('saved_ratings.csv')


# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population)
# и сохранить ее в переменную avg.
import pandas as pd
file='california_housing_train.csv'
df=pd.read_csv(file)
avg=df[(df['population']>0)&(df['population']<=500)]['median_house_value'].mean()
print(avg)


# pip install pandas
import pandas as pd
# california_housing_train.csv
file = 'california_housing_train.csv'
df = pd.read_csv(file)
# print(df)

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.dtypes)
# print(df.isnull())
# print(df.isnull().sum())
# print(df[['median_house_value', 'median_income']])
# print(df['median_house_value'])
# print(df.loc[df.median_income < 2, ['median_house_value', 'median_income']])
# df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]
# print(df[df['housing_median_age'] < 20]['total_bedrooms', 'total_rooms'])

# print(df[['longitude', 'latitude']])
# print(df.iloc[: , 0:2])
# Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000
# print(df.loc[(df.housing_median_age < 7) & (df.median_house_value > 70000), ['housing_median_age', 'median_house_value']])
# print(df.loc[(df.housing_median_age < 7) & (df.median_house_value > 70000)])
# print(df.loc[(df.housing_median_age < 7) & (df.median_house_value > 360000) & (df.median_house_value < 400000), ['housing_median_age', 'median_house_value']])
# df2 = df[(df.housing_median_age < 7) & (df.median_house_value > 360000) & (df.median_house_value < 400000)]

# df2=df['median_house_value'][(df['housing_median_age'] < 20)&(df['median_house_value'] > 70000)]
# print(df2)
# df2.to_csv('new_data2.csv')
# df2.to_excel('new.xlsx')

# print(df.median_house_value.max(), df.median_house_value.min())
# print(df['median_house_value'].max(), df['median_house_value'].min())
# print(df['median_house_value'].median(), df['median_house_value'].mean())

# [1, 2, 3, 4, 20, 50]
# dff = pd.DataFrame({'data': [1, 2, 3, 15, 20, 50], 'ddd': [2, 5, 6, 7, 9, 2]})
# print(dff['data'])
# print(dff['data'].median(), dff['data'].mean())

# avg = df['median_house_value'].median(), df['median_house_value'].mean()

# Показать максимальное median_house_value, где
# median_income = 3.1250
# print(df.loc[df.median_income == 3.125, ['median_house_value', 'median_income']])
# print(df.loc[df.median_income == 3.125, ['median_house_value']].max())
# df2=df['median_house_value'][(df['median_income'] == 3.125)]
# print(df2.max())
# print(df['median_house_value'][(df['median_income'] == 3.125)].max())

# Узнать какая максимальная population в зоне
# минимального значения median_house_value
# print(df.median_house_value.min())
print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']])
# print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']].max())
#
print(df['population'][(df['median_house_value'] == df['median_house_value'].min())].max())
#
# print('*' * 15)
# print(df.median_house_value.min())
# print(df.median_house_value.max())
# print(df.median_house_value.quantile(.01))
#
# print(df.loc[df.median_house_value <= df.median_house_value.quantile(.01), ['population']])
# print(df.loc[df.median_house_value <= df.median_house_value.quantile(.05), ['population']].max())

# df1 = df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']]
# df1.to_csv('new_data1.csv')
#
# df2 = df[['median_house_value', 'population']]
# print(df2)
# print(type(df2))
# df2.to_csv('new_data.csv')


