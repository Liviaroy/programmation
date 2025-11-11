temperatures = [23.5, 25.4, 27.6, 24.9, 26.7, 24.6]
print(f"Temperatures: {temperatures}")

#extreme
temperatures.sort()
min_temp = temperatures[0]
max_temp = temperatures[-1]
print(f"        min : {min_temp}")
print(f"        max : {max_temp}")


#moyenne
somme = sum(temperatures)
nombre = len(temperatures)
moy = somme/nombre
print(f"    moyenne : {moy}")

#nombre de mesure
mesure = len(temperatures)
print(f"  nb.mesure : {mesure}")
