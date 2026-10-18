import pandas as pd 

data = pd.read_csv('customers-100.csv')
print(data)
print (data.head(10))
print(data.tail(10))

print(pd.options.display.max_rows)

pd.options.display.max_rows = 2000

x = data.dropna()

data.dropna(inplace=True)

data.fillna(0,inplace=True)
print(data)

print ("mean: ",data['Index'].mean())
print ("median: ",data['Index'].median())
print ("mode: ",data['Index'].mode()[0])