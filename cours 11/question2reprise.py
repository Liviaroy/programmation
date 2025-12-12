import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tips_dataset.csv")
print(df.head())

df["tip_personne"] = df["tip"] / df["size"]
print(df.head())

df["tip_personne"].hist(bins=20) # Diviser les données en 20 intervalles égaux
plt.title("Distribution du pourboire par personne")
plt.xlabel("Pourboire par personne")
plt.ylabel("Fréquence")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()

df.boxplot(column="tip_personne", by="size")
plt.title("Pourboire par personne en fonction de la taille du groupe")
plt.suptitle("")
plt.xlabel("Taille du groupe")
plt.ylabel("Pourboire par personne")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()

