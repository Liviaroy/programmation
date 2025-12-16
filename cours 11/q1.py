import pandas as pd
df = pd.read_csv("mpg_dataset.csv")

df_q1 = df[(df['origin'] == 'japan') & (df['acceleration'] >= 19.4)]
print(f"Les modèles japonais ayant une accélération plus grande ou égale à 19.4 :")
for index, row in df_q1.iterrows():
    print(f"  - {row['name']}")

df_q2 = df.sort_values('horspower', ascending = False).head(5)
print(f"Les cinq voiture avec le plus de horsepower :")
for index, row in df_q2.iterrows():
    print(f" horsepower : {row['horspower']} - {row['name']}")
