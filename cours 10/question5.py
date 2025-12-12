import csv

resultat1=[]
resultat2=[]
resultat3=0

with open("Turing.csv", "r") as f:
    lecteur_csv = csv.reader(f)
    next(lecteur_csv)
    compteur = 0
    annee_precedente = 0
    for ligne in lecteur_csv:
        if "intelligence" in ligne[2]:
            resultat1.append(ligne[1])
        resultat3 += 1
        if annee_precedente != 0:
            compteur = 1
        else:
            compteur += 1
            if compteur == 3:
                resultat1.add(ligne[0])
        annee_precedente = ligne[0]








print(f"Nombre total de lauréats :{resultat3}")
print()
print(f"Lauréats avec 'intellligence dans la contribution :")
for laureat in resultat2:
    print(laureat)
print()
print(f"Années avec 3 lauréats ou plus :")
for annee in resultat1:
    print(annee)


"""
Nombre total de lauréats : 79

Lauréats avec 'intelligence' dans la contribution :
Marvin Minsky
Allen Newell
Herbert A. Simon
Raj Reddy

Années avec 3 lauréats ou plus :
2002
2007
2018
"""