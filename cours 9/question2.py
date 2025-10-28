virus = ["Virus-T", "Virus-C", "Virus-G", "Uroboros"]

if len(virus) == 0:
    print("Désolé aucun produit pharmaceutique mortel disponible")

else:
    print(f"Liste des {len(virus)} virus :")
    for v in virus:
        print(f"  {v}  ")

