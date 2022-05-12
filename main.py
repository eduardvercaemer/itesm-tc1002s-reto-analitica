import matplotlib.pyplot as plt
import pandas as pd

# preguntas

### Qué datos hay que seleccionar ?
#
# nosotros vamos a trabajar con los datos de varios grupos, a lo largo de los
# años 1960 - 2020

### Hay que eliminar o reemplazar valores en blanco ?
#
# vamos a eliminar los valores en blanco, porque no nos interesan

### Es posible agregar más datos ?
#
# podriamos calcular valores como media, minimos o maximos, pero
# no nos interesan demasiado

### Hay que integrar o fusionar datos de varias fuentes ?
#
# nosotros solo consideramos los datos originales

### Es necesario ordenar los datos para el análisis ?
#
# vamos a ordenar los datos de acuerdo al valor en el año 2020, para asi
# obtener los grupos mas representativos

### Tengo que hacer conjuntos de datos para entrenamiento y prueba ?
#
# no vamos a utilizar conjuntos de datos para entrenamiento y prueba

### Qué ajustes se tuvieron que hacer a los datos ?
#
# se renombraron las columnas y se transpuso la tabla para hacer mejor
# visualizacion de los datos

# cargar datos
data = pd.read_csv("Countries GDP 1960-2020.csv")

# renombrar columnas por paises
data.set_axis(data['Country Name'], axis=0, inplace=True)
# ordenar por año 2020 descendente
data.sort_values('2020', inplace=True, ascending=False)
# tomamos los datos de los primeros 10 grupos
top = data.head(n=10)
# transponemos la tabla y graficamos todos los años
top[top.columns[2:]].transpose().plot()
plt.show()


# análisis

### ¿Hay alguna variable que no aporta información?
#
# En nuestro caso, no realmente, solo tenemos una variable, el gdp.

### Si tuvieras que eliminar variables, ¿Cuáles quitarías y por qué?
#
# No podemos eliminar ninguna variable, ya que todas las variables son
# independientes. En cualquier caso, borraria los datos de ciertos grupos,
# como gdp por regiones, etc.

### ¿Existen variables que tengan datos extraños?
#
# Analisando la grafica de los grupos con mayor gdp, los datos tienen sentido
# y no aperece haber datos extraños

### Si comparas las variables, ¿todas están en rangos similares? ¿Crees que esto afecte?
#
# Podemos hacer una comparacion de los grupos mas grandes y los mas pequeños:
"""
top = data.head()
bot = data.tail()
top_bot = pd.concat([top, bot])
top_bot[top_bot.columns[2:]].transpose().plot()
plt.show()
"""
# Y esta claro que el rango de valores es muy grande para distintos paises,
# esto significa que podemos analisar diversos grupos de datos

### ¿Puedes encontrar grupos qué se parezcan? ¿Qué grupos son éstos?
#
# Sí, por ejemplo, los grupos con mayor gdp en el año 2020, son los grupos
# que incluyen muchos paises, como regiones continentales, o el gdp combinado
# del mundo, etc

# analisis de 'caja' para gdp en el 2020

gdp_2020 = data['2020']
# create box graph
gdp_2020.plot(kind='box')
plt.show()

# analisis de 'heatmap' para gdp en el 2020

plt.figure(figsize=(10, 10))
plt.title('GDP')
plt.ylabel('Year')
plt.xlabel('Countries')
plt.imshow(data[data.columns[2:]].transpose(), cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()
