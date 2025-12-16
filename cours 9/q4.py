# Liste des espèces marines observées dans la zone Atlantique
zone_atlantique = ["morue", "homard", "maquereau", "phoque"]

# Liste des espèces marines observées dans la zone Pacifique
zone_pacifique = ["saumon", "morue", "otarie", "maquereau"]

liste_combinee = set(zone_atlantique + zone_pacifique)
print(liste_combinee)