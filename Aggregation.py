import pandas as pd 

df = pd.DataFrame([("Hungry Howies Pizza","beef",12.99,8,4),
	("Brickyard Pizza","Peperoni",9.99, 6, 4),
	("Carrabbas Italian Grill", "Sausage", 10.99, 8, 2),
	("Little Caesars Pizza", "beef", 5.99, 4, 2),
	("Mikes Pizza", "Cheese", 6.99, 6, 3),
	("Theos Neighborhood Pizza","Peperoni", 7.99, 8, 6),
	("Salvos Pizzabar","beef", 9.99, 8, 4)],
	columns=("Name","Class","Price","Slices","Dips"))

print(df)

print(df.count())
print(df[["Class"]].count())
print(df.sum())
print(df[["Price"]].sum())

print(df[['Dips']].min())
print(df[['Slices']].max())
print(df.mean())
print(df.median())


#Groupby in action

print(df.groupby('Class').sum())

print(df.groupby('Class').sum().Price)
