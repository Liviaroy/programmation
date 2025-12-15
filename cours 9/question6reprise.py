virus = ["Virus-T", "Virus-C", "Virus-G", "Uroboros"]
caracteristiques = [
    "Transforme les humains en zombies et armes biologiques",
    "Provoque des mutations extrêmes et régénère les tissus",
    "Cause des mutations incontrôlables avec régénération cellulaire rapide",
    "Consomme les organismes incompatibles et renforce les hôtes compatibles"
]

print(f"Liste des {len(virus)} virus :")

if len(virus) == 0:
    print(f" Désolé aucun produit pharmaceutique mortel disponible!")
else:
    for i in range(len(virus)):
        print(f"  {virus[i]} : {caracteristiques[i]}")

