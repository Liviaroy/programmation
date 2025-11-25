import csv
import pandas as pd

df = pd.read_csv('tips_dataset.csv')
print(df.head(10))
print(df.describe())

tip_smoker = df.groupby('smoker')['tip'].agg(['mean'])
print(tip_smoker)

tip_day = df.groupby('day')['tip'].agg(['mean'])
print(tip_day)

tip_temps = df.groupby('time')['tip'].agg(['mean'])
print(tip_temps)

tip_size = df.groupby('size')['tip'].agg(['mean'])
print(tip_size)

#la variable qui semble le plus influencer le montant du pourboire est la taille des groupes
#la variable qui n'influence pas le pourboir est si le client est fumeur ou non
