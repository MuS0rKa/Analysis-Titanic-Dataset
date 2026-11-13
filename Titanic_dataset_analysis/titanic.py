import pandas as pd

titanic = pd.read_csv("data/Titanic-Dataset.csv")
print(titanic.groupby("Sex")["Survived"].sum())