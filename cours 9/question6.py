# Liste des espèces marines observées dans la zone Atlantique
zone_atlantique = ["morue", "homard", "maquereau", "phoque"]

# Liste des espèces marines observées dans la zone Pacifique
zone_pacifique = ["saumon", "morue", "otarie", "maquereau"]

liste_combinee = zone_atlantique + zone_pacifique
ensemble = set(liste_combinee)
liste_sans_doublon = list(ensemble)

print(liste_combinee)
print(ensemble)

print(f"Espèces recensées : {liste_sans_doublon}")