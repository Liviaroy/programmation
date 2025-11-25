import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mpg_dataset.csv')
df.head()

df["l_par_100km"] = df["mpg"]/100
df.head()
print(df.head())

df.boxplot(column="l_par_100km", by="origin")
plt.title("Consommation d'essence (L/100km) en fonction de l'origine du véhicule")
plt.xlabel("Origine du véhicule")
plt.ylabel("Consommation d'essence (L/100km)")
plt.suptitle("")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()


df.boxplot(column="l_par_100km", by="model_year")
plt.title("Consommation d'essence (L/100km) en fonction de l'origine du véhicule")
plt.xlabel("Année de fabrication")
plt.ylabel("Consommation d'essence (L/100km)")
plt.suptitle("")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()