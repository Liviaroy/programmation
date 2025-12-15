# Liste des espèces marines observées dans la zone Atlantique
zone_atlantique = ["morue", "homard", "maquereau", "phoque"]

# Liste des espèces marines observées dans la zone Pacifique
zone_pacifique = ["saumon", "morue", "otarie", "maquereau"]

espece_combinee = zone_atlantique + zone_pacifique
espece_triee = set(espece_combinee)
print(espece_triee)