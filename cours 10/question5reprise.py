import csv

annee = []
Laureat = []
contribution = []
affiliation = []

with open("Turing.csv", "r") as f:
    lecteur_csv = csv.reader(f)
    next(lecteur_csv)  # Ignorer la ligne d'en-tête
    for ligne in lecteur_csv:
        annee.append(ligne[0])
        Laureat.append((ligne[1])) # Conversion en nombre flottant
        contribution.append((ligne[2]))   # Conversion en nombre flottant
        affiliation.append((ligne[3]))
    for ligne in lecteur_csv:
        if "intelligence" in ligne[2]:
            Laureat.append(ligne[1])
            contribution += 1
            print(Laureat)




print(len(Laureat))

