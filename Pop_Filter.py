import pandas as pd

a = open("population.csv", "r")
print(a.read())

file = pd.read_csv("population.csv")
print(file.info())

print(file.describe())

mil = file[file["Value"] >5000000]
print("Above 5 million pop", mil)

file.to_csv("Pop_Large.csv", index = True)