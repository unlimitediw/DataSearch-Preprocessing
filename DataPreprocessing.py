'''
Population, City Name, Country name, latitude and longitude
'''
import pandas as pd

data = pd.read_csv('./Data/ergebnis.csv')
newData = data.drop(labels=['the_geom', 'original_name', 'cartodb_id', 'created_at', 'updated_at'], axis=1)
newData = pd.DataFrame(newData)
newData.to_csv('./Data/newData.csv')

