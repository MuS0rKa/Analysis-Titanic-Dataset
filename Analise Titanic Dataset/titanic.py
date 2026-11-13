import pandas as pd

titanic = pd.read_csv("Titanic-Dataset.csv")
print(titanic.groupby("Sex")["Survived"].sum())