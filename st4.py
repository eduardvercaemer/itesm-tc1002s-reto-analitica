import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# load all data
data = pd.read_csv("Countries GDP 1960-2020.csv")
data.set_axis(data['Country Name'], axis=0, inplace=True)
data.sort_values('2020', inplace=True, ascending=False)

# get selection of data


def country_gdp(country):
    return data[data.columns[2:]].transpose()[country]


countries = ['Mexico', 'Colombia', 'Peru', 'Chile']
gdps = [country_gdp(country) for country in countries]
models = [LinearRegression().fit(gdp.index.values.reshape(-1, 1),
                                 gdp.values.reshape(-1, 1)) for gdp in gdps]
def predict(model):
  years = range(2021, 2030)
  years = np.array(years).reshape(-1, 1)
  return model.predict(years).reshape(-1)

predictions = [predict(model) for model in models]

fig = plt.figure()
for country, gdp, prediction in zip(countries, gdps, predictions):
  ax = fig.add_subplot(2, 2, countries.index(country) + 1)
  ax.xaxis.set_major_locator(plt.MultipleLocator(15))
  gdp_y = gdp.values.reshape(-1)
  gdp_x = [int(x) for x in gdp.index.values.reshape(-1)]
  ax.plot(gdp_x, gdp_y, label='GDP')
  prediction_y = prediction
  prediction_x = list(range(2021, 2030))
  ax.plot(prediction_x, prediction_y, label='Prediction')
  ax.set_title(country)
  ax.legend()

plt.show()
