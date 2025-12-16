import pandas as pd

df = pd.read_csv("tips_dataset.csv")
df.head()
df.describe()

#i
tip_smoker = df.groupby("smoker")["tip"].mean()
print(tip_smoker)

#ii
tip_jour = df.groupby("day")["tip"].mean()
print(tip_jour)

#iii
tip_time = df.groupby("time")["tip"].mean()
print(tip_time)

#iv
tip_size = df.groupby("size")["tip"].mean()
print(tip_size)

# c'est plus payant quand c'est un plus gros groupe
# si le client est fumeur ou non-fumeur n'influence pas le pourboire qu'il laisse au serveur
