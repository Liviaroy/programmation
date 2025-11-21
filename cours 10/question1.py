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


liste_mois = [t[0] for t in temperatures]
liste_temperatures = [t[1] for t in temperatures]


plt.plot(liste_mois, liste_temperatures, marker='o', color='green')
plt.ylabel("Températures moyenne (C)")
plt.xlabel("mois")
plt.grid(alpha=0.5, linestyle='--')
plt.title("Temperatures moyenne mensuelle dans la réserve naturelle")
plt.show()