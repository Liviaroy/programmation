#numero1
virus = ["Virus-T", "Virus-C", "Virus-G", "Uroboros",]

if len(virus) == 0:
    print(f"Désolé aucun virus diponible pour le moment :(")
#si la longueur de la liste est 0 element afficher ce message(La liste a aucun virus)
else :
    longueur_liste = len(virus)
    print(f"Liste des {longueur_liste} virus:") #affiche le nombre d'élements de la liste
    for v in virus:
        print(f"  {v}  ")
#boucle, pour tout les elément de la liste afficher les éléments"""


"""CONTRAINTES À RESPECTER
Votre code doit fonctionner peu importe le nombre d'éléments dans la liste.
Vous devez utiliser un for element in liste pour parcourir les éléments de la liste.
Vous pouvez modifier le contenu de la liste fournie pour tester différents scénarios.
Si la liste est vide, afficher un message sympa à l'utilisateur.
Liste des 4 virus :
  Virus-T
  Virus-C
  Virus-G
  Uroboros"""
#numero2
temperatures = [23.5, 25.4, 27.6, 24.9, 26.7, 24.6]
min_temp = temperatures[0]
max_temp = temperatures[0]
nb_element = 0
for temp in temperatures:
    nb_element += 1
    if temp < min_temp:
        min_temp = temp
    if temp > max_temp:
        max_temp = temp
print(min_temp)
print(max_temp)

moyenne = (max_temp + min_temp) / 2
print(moyenne)
#numero3
temperatures = [23.5, 25.4, 27.6, 24.9, 26.7, 24.6]
temperatures_trie = sorted(temperatures)
max_temp = temperatures_trie[0]
min_temp = temperatures_trie[-1]
longueur_liste = len(temperatures)
somme = sum(temperatures)
moyenne = somme/longueur_liste
print(f"Températures : {temperatures}")
print(f"         min : {min_temp}")
print(f"         max : {max_temp}")
print(f"     moyenne : {moyenne}")
print(f" nb. mesures : {longueur_liste}")

#numero4
# Liste des espèces marines observées dans la zone Atlantique
zone_atlantique = ["morue", "homard", "maquereau", "phoque"]

# Liste des espèces marines observées dans la zone Pacifique
zone_pacifique = ["saumon", "morue", "otarie", "maquereau"]

combine = zone_atlantique + zone_pacifique
combine_sans_doublon = set(combine)
print(f"Espèces rescensées : [{combine_sans_doublon}]")

#numero5
virus = ["Virus-T", "Virus-C", "Virus-G", "Uroboros"]
caracteristiques = [
    "Transforme les humains en zombies et armes biologiques",
    "Provoque des mutations extrêmes et régénère les tissus",
    "Cause des mutations incontrôlables avec régénération cellulaire rapide",
    "Consomme les organismes incompatibles et renforce les hôtes compatibles"
]

for i in range (len(virus)):
    print(f"{virus[i]} : {caracteristiques[i]}")

#numero6
virus_et_autres_info = [
    ["Virus-T", 0.9 ,"Transforme les humains en zombies et armes biologiques"],
    ["Virus-C", 0.0001 ,"Provoque des mutations extrêmes et régénère les tissus"],
    ["Virus-G", 0.85, "Cause des mutations incontrôlables avec régénération cellulaire rapide"],
    ["Uroboros", 0.005, "Consomme les organismes incompatibles et renforce les hôtes compatibles"]
]
nb_element = len(virus_et_autres_info)
if nb_element > 0:    #si la liste n'est pas vide afficher le nombre d'élement
    print(f"Liste des {nb_element} virus:")
    for v in virus_et_autres_info:
        print(f"  {v[0]} - {v[2]} : (taux de mutation : {v[1]*100}%)")

