populations = {
    "Cerfs": [32, 45, 50, 41],
    "Renards": [12, 15, 13, 10],
    "Lapins": [85, 102, 98, 76],
    "Aigles": [5, 7, 6, 5]
}
saisons = ["Printemps", "Été", "Automne", "Hiver"]

nb_element = len(populations.items())

print(f"Recensement pour les {nb_element} espèces :")
print()

nom_espece_moyenne_max = ""
moyenne_max = 0


for cle, valeur in populations.items():
    moyenne = sum(valeur) / len(valeur)

    if moyenne > moyenne_max:
        moyenne_max = moyenne
        nom_espece_moyenne_max = cle

    print(f"{cle} : moyenne par saison = {moyenne} individus")

print()
print(f"Espèce la plus nombreuse : {nom_espece_moyenne_max} ({moyenne_max} individus en moyenne)")



