import matplotlib.pyplot as plt
secteurs = ["Résidentiel", "Agricole", "Industriel", "Énergie", "Municipal", "Autres"]
couleur_barres = ['skyblue', 'limegreen', 'gold', 'salmon', 'orchid', 'gray']

# Données totales pour l’ensemble du Canada (une données par province/territoire)
residentiel = [410, 380, 220, 200, 890, 860, 170, 180, 60, 100, 40, 30, 25]
agricole = [780, 640, 850, 600, 720, 670, 230, 210, 150, 180, 20, 15, 10]
industriel = [520, 410, 290, 310, 1100, 970, 190, 200, 50, 130, 60, 40, 20]
energie = [300, 270, 180, 150, 400, 420, 100, 110, 30, 90, 25, 20, 10]
municipal = [260, 250, 130, 120, 680, 700, 90, 100, 25, 70, 15, 10, 8]
autres = [90, 80, 60, 50, 130, 120, 40, 40, 10, 25, 5, 5, 3]

total = []
total.append((sum(residentiel))/len(residentiel))
total.append((sum(agricole))/len(agricole))
total.append((sum(industriel))/len(industriel))
total.append((sum(energie))/len(energie))
total.append((sum(municipal))/len(municipal))
total.append((sum(autres))/len(autres))

plt.bar(secteurs, total, color = couleur_barres)
plt.title("Consommation moyenne d'eau par secteur au Canada")
plt.xlabel("Secteur")
plt.ylabel("Consommation moyenne(millions de  m3/an)")
plt.grid(axis = "y", linestyle = "--")
plt.show()

