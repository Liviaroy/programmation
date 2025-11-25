import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips_dataset.csv')
print(df.head())

df["tip_par_personne"] = df["tip"] / df["size"]
print(df.head())
#histogramme
df["tip_par_personne"].hist(bins=20)
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.title("Distribution du pourboire par personne")
plt.xlabel("Pourboire par personne")
plt.ylabel("Fréquence")
plt.show()
#boite a moustache
df.boxplot(column="tip_par_personne", by="size")
plt.title("Pourboire par personne en fonction de la taille du groupe")
plt.xlabel("Taille du groupe")
plt.ylabel("pourboire par personne")
plt.suptitle("")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()
