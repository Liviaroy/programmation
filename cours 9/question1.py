import matplotlib.pyplot as plt

transport = ["Bus", "Voiture", "Vélo", "Skateboard", "Trottinette", "Marche"]
etudiants = [40, 30, 20, 15, 10, 5]

plt.bar(transport, etudiants)

plt.title("Comment les étudiants viennent au cégep")
plt.xlabel("Mode de transport")
plt.ylabel("Nombre d'étudiants")

plt.show()