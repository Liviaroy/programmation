import pandas as pd

df = pd.read_csv("mpg_dataset.csv")
"""Les modèles japonais ayant une accélération de 19.4 et plus :
    - toyota corolla 1200
    - mazda glc deluxe
    - datsun 210 mpg

Les 5 voitures avec le plus de horsepower :
    - horsepower : 230.0 - pontiac grand prix
    - horsepower : 225.0 - buick electra 225 custom
    - horsepower : 225.0 - pontiac catalina
    - horsepower : 225.0 - buick estate wagon (sw)
    - horsepower : 220.0 - chevrolet impala

Le nombre de voitures japonaises avec un poid supérieur à 2500 : 17"""

df_1 = df[(df['origin'] == 'japan') & (df['acceleration'] >= 19.4)]
print(f"Les modèles japonais avec un accélération de 19.4 et plus :")
for index, row in df_1.iterrows():
    print(f"   - {row['name']}")
print()
df_2 = df.sort_values('horsepower', ascending = False).head(5)
print(f"Les voitures avec le plus de horsepower :")
for index, row in df_2.iterrows():
    print(f"   - horsepower : {row['horsepower']} - {row['name']}")
print()
df_3 = df[(df['origin'] == 'japan') & (df['weight'] > 2500)]
print(f"Le nombre de voitures japonaises avec un poid supérieur à 2500 : {len(df_3)}")

