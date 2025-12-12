import matplotlib.pyplot as plt

populations = {
    "Cerfs": [32, 45, 50, 41],
    "Renards": [12, 15, 13, 10],
    "Lapins": [85, 102, 98, 76],
    "Aigles": [5, 7, 6, 5]
}
saisons = ["Printemps", "Été", "Automne", "Hiver"]

#etape 1
cle = populations.items()
moyenne_max = 0
recensement_max = ""
print(f"Recensement pour les {len(cle)} espèces:")
print()

for cle,valeur in populations.items():
    moyenne = sum(valeur) / len(valeur)

    if moyenne > moyenne_max:
        moyenne_max = moyenne
        recensement_max = cle
    print(f"{cle}: moyenne par saison = {moyenne} individus")
print()
print(f"Espèce la plus nombreuse : {cle} ({moyenne_max} individus en moyenne)")

#graphique
plt.plot(saisons, populations["Cerfs"], marker='o', color='blue')
plt.plot(saisons, populations["Renards"], marker='o', color='orange')
plt.plot(saisons, populations["Lapins"], marker='o', color='green')
plt.plot(saisons, populations["Aigles"], marker='o', color='red')

plt.legend()
plt.grid(alpha = 0.8, linestyle = '--')
plt.xlabel("Saison")
plt.ylabel("Nombre d'individus")
plt.title("Évolution des populations selon les saisons")
plt.show()