import matplotlib.pyplot as plt
populations = {
    "Cerfs": [32, 45, 50, 41],
    "Renards": [12, 15, 13, 10],
    "Lapins": [85, 102, 98, 76],
    "Aigles": [5, 7, 6, 5]
}
saisons = ["Printemps", "Été", "Automne", "Hiver"]

pop_cerf = populations["Cerfs"]
pop_renard = populations["Renards"]
pop_lapin = populations["Lapins"]
pop_aigles = populations["Aigles"]
#moyenne
moy_cerf = sum(pop_cerf) / len(pop_cerf)
moy_renard = sum(pop_renard) / len(pop_renard)
moy_lapin = sum(pop_lapin) / len(pop_lapin)
moy_aigles = sum(pop_aigles) / len(pop_aigles)

nb_espece = populations.items()
max_espece = 0
moy_espece = 0
espece_max = ''
print(f"Rescencement pour les {len(nb_espece)} espèces : ")
print()
for cle, valeur in populations.items():
    moyenne = sum(valeur) / len(valeur)
    if moyenne > max_espece:
        max_espece = moyenne
        espece_max = cle
    print(f"{cle} : moyenne par saison : {moyenne} individus")
print()
print(f"Espèce la plus nombreuse : {espece_max} ({max_espece} individus en moyenne)")

plt.plot(saisons, pop_cerf, color='blue', label= "Cerfs", marker='o')
plt.plot(saisons, pop_renard, color = 'orange', label = "Renards", marker='o')
plt.plot(saisons, pop_lapin, color = 'green', label = "Lapins", marker='o')
plt.plot(saisons, pop_aigles, color = 'red', label = "Aigles", marker='o')
plt.title("Évolution des populations selon les saisons")
plt.ylabel("Nombre d'individus")
plt.xlabel("Saison")
plt.legend()
plt.grid(alpha = 0.8)
plt.show()
