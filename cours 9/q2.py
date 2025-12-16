temperatures = [23.5, 25.4, 27.6, 24.9, 26.7, 24.6]

"""La température la plus basse
La température la plus élevée
La température moyenne
Le nombre de mesures prises"""

nb_element = 0
min_temp = temperatures[0]
max_temp = temperatures[-1]
somme = 0
moyenne = 0
for t in temperatures:
    somme += t
    if t < min_temp:
        min_temp = t
    if t > max_temp:
        max_temp = t
    nb_element += 1
    moyenne = somme / nb_element
print(f"Températures : {temperatures}")
print(f"         min : {min_temp}")
print(f"         max : {max_temp}")
print(f"     moyenne : {moyenne}")
print(f"  nb.element : {nb_element}")