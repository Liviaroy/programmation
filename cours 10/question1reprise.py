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

mois = [t[0] for t in temperatures]
temperature = [t[1] for t in temperatures]

plt.plot(mois, temperature, color='green', marker='o')
plt.grid(alpha = 0.5, linestyle = '--')
plt.xlabel("Mois")
plt.ylabel("Température moyenne (°C)")
plt.title("Température moyenne mensuelle dans la réserve naturelle")
plt.show()