import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd

#Apples and oranges data set
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
apples = [0.89, 0.72, 0.82, 0.49, 0.30, 0.79, 1.08]
oranges = [0.99, 0.86, 0.82, 0.73, 0.12, 0.90, 0.80]

plt.plot(years, apples, marker = "o")
plt.plot(years, oranges, marker = "o")
plt.xlabel('Years')
plt.ylabel("Apples")
plt.title("Apple and Orange Production Over Years")
plt.legend(['apples', 'oranges'])

#Calling from "tips" data base
tips_df = sns.load_dataset("tips")
print(tips_df)
sns.barplot(x="day", y="total_bill", hue = 'Sex', data=tips_df)

#Calling from "flowers" data base
flo_df = sns.load_dataset("iris")
print(flo_df)
plt.title("Iris Dataset Histogram")
plt.hist(flo_df.petal_length, bins=5)

flo_df = sns.load_dataset("iris")
sns.pairplot(flo_df, hue= 'species')

#Heatmap of flower species data
flo_df['species'] = pd.factorize(flo_df['species'])[0]
correlation_matrix = flo_df.corr()
sns.heatmap(correlation_matrix, annot=True)

plt.show()