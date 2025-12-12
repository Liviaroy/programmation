import pandas as pd

df = pd.read_csv("tips_dataset.csv")
print(df.head(10))
print(df.describe())

tip_smoker = df.groupby('smoker')['tip'].mean()
print(tip_smoker)

tip_jour = df.groupby("day")['tip'].mean()
print(tip_jour)

tip_time = df.groupby('time')['tip'].mean()
print(tip_time)

tip_size = df.groupby('size')['tip'].mean()
print(tip_size)

#la taille du groupe semble influencer le plus le pourboire
#si le client est fumeur ou non-fumeur n'influence pas le montant de pourboire
