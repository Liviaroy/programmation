import matplotlib.pyplot as plt

temperatures = [
    ("Janvier", 2.5),
    ("Février", 3.0),
    ("Mars", 6.2),
    ("Avril", 10.5),
    ("Mai", 15.3),
    ("Juin", 19.1),
    ("Juillet", 22.4),
    ("Août", 21.9),
    ("Septembre", 17.0),
    ("Octobre", 12.1),
    ("Novembre", 6.8),
    ("Décembre", 3.4)
]
liste_temperatures = []
for t in temperatures:
    liste_temperatures.append(t[1])

liste_mois = []
for mois in temperatures:
    liste_mois.append(mois[0])

print(liste_temperatures)
print(liste_mois)

plt.plot(liste_mois, liste_temperatures, color='green', marker='o')
plt.title("Température moyenne mensuelle dans la réserve naturelle")
plt.ylabel("Température moyenne(°C)")
plt.xlabel("Mois")
plt.grid(alpha = 0.5, linestyle = '--')
plt.show()