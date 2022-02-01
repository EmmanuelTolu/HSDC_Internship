import pandas as pd
df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG.csv")

#What is the total sum of Animal Fat produced in 2014 and 2017 respectively?
df.groupby('Item')['Y2014'].agg(['sum','count'])
df.groupby('Item')['Y2017'].agg(['sum','count'])

#What is the mean and standard deviation across the whole dataset for the year 2015 to 3 decimal places?
mean = round(df['Y2015'].mean(), 3)
std = round(df['Y2015'].std(), 3)

#What is the total number and percentage of missing data in 2016 to 2 decimal places?
percent_missing = df.isnull().sum() * 100 / len(df)

#Which year had the highest correlation with ‘Element Code’?
c = df.corr()
c['Element Code'].nlargest(2)

#What year has the highest sum of Import Quantity?
IQ = df.groupby('Element')['Y2017'].agg(['sum','count'])

#What is the total number of the sum of Production in 2014?
SoP = df.groupby('Element')['Y2014'].agg(['sum', 'count'])

#Which of these elements had the highest sum in 2018?
Hs = df.groupby('Element')['Y2018'].agg(['sum', 'count'])

#Which of these elements had the lowest sum in 2018?
Ls = df.groupby('Element')['Y2018'].agg(['sum', 'count'])

#What is the total Import Quantity in Algeria in 2018?
fg = df[df["Area"].str.contains("Algeria")==True]
mi = fg.groupby('Element')['Y2018'].agg(['sum','count'])
mi['sum'].min()

#What is the total number of unique countries in the dataset?
df['Area'].nunique()
