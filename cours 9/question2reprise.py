temperatures = [23.5, 25.4, 27.6, 24.9, 26.7, 24.6]

temp_min = temperatures[0]
temp_max = temperatures[-1]
nb_element = 0
for temp in temperatures:
    nb_element += 1
    if temp < temp_min:
        temp_min = temp
    if temp > temp_max:
        temp_max = temp

moyenne = (temp_min + temp_max) / 2
print(f"Température : {temperatures}")
print(f"        min : {temp_min}")
print(f"        max : {temp_max}")
print(f"    moyenne : {moyenne}  ")
print(f" nb.element : {nb_element}")
