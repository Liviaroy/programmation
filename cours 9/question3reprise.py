temperatures = [23.5, 25.4, 27.6, 24.9, 26.7, 24.6]

max_temp = max(temperatures)
min_temp = min(temperatures)
moyenne = sum(temperatures) / len(temperatures)
nb_element = len(temperatures)

print(f"Températures : {temperatures}")
print(f"         max : {max_temp}")
print(f"         min : {min_temp}")
print(f"     moyenne : {moyenne}")
print(f"  nb.element : {nb_element}")
