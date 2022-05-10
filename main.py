import pandas as pd

# cargar datos
data = pd.read_csv("Countries GDP 1960-2020.csv")

# observar datos iniciales
print(data.head())

# cantidad de paises
print("paises: ", len(data.index))

# maximos, minimos, etc, de cada año
print(data[data.columns[2:]].describe())

# paises y su gdp en 2020
print(data[["Country Name", "2020"]])

