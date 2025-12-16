import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mpg_dataset.csv")

df["l_100_km"] = 235.215 / df["mpg"]

df.boxplot(column="l_100_km", by="origin")
plt.title("Consommation d'essence (L/100km) en fonction de l'origine du véhicule")
plt.suptitle("")
plt.xlabel("Origine")
plt.ylabel("Consommation d'essence (L/100km)")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()

df.boxplot(column="l_100_km", by="model_year")
plt.title("Consommation d'essence (L/100km) en fonction de l'année de fabrication de son modèle")
plt.suptitle("")
plt.xlabel("Année de fabrication")
plt.ylabel("Consommation d'essence (L/100km)")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()