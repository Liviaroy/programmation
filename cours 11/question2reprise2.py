import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tips_dataset.csv")

df["tip_par_personne"] = df["tip"] / df["size"]

df["tip_par_personne"].hist(bins=20)
plt.title("Distribution du pourboire par personne")
plt.xlabel("Pourboire par personne")
plt.ylabel("Fréquence")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()

df.boxplot(column="tip_par_personne", by="size")
plt.title("Pourcentage de pourboire par personne")
plt.suptitle("")
plt.xlabel("Taille du groupe")
plt.ylabel("Pourboire par personne")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()