import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mpg_dataset.csv")
print(df.head())

df["litre_cent"] = 235.215 / df["mpg"]

df.boxplot(column="litre_cent", by="origin")
plt.title("Consommation d'essence (L/100km) en fonction de l'origine du véhicule")
plt.suptitle("")  # Supprimer le titre autogénéré apparaisant en haut de notre titre (il indique le regroupement réalisé)
plt.xlabel("Origine du véhicule")
plt.ylabel("Consommation d'essence (L/100km)")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()

df.boxplot(column="litre_cent", by="model_year")
plt.title("Consommation d'essence (L/100km) en fonction de l'année de fabrication")
plt.suptitle("")
plt.xlabel("Année de fabrication")
plt.ylabel("Consommation d'essence (L/100km)")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()