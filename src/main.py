import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

#read input
print("Toy datasets:")
print("1. iris")
print("2. wine")
print("3. breast_cancer")
num = int(input("input a number: "))
data = datasets.load_iris()
if num == 2:
    data = datasets.load_wine()
elif num == 3:
    data = datasets.load_breast_cancer()
    

#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

#visualisasi hasil ConvexHull
#from scipy.spatial import ConvexHull
from myConvexHull import myConvexHull

#sepal
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title(data.feature_names[0] + " vs " + data.feature_names[1])
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasiConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
plt.show()

#petal
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title(data.feature_names[2] + " vs " + data.feature_names[3])
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[2,3]].values
    hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasiConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
plt.show()