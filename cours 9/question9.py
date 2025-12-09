liste = [1, 2, 3, 4, 5]

liste1 = [l * 5 for l in liste]
print(liste1)

liste2 = [x + 3 for x in liste]
print(liste2)

liste3 = [v ** 2 for v in liste]
print(liste3)

liste4 = [str(i) for i in liste]
print(liste4)

liste5 = [y * 2 for y in liste if y%2 == 0]
print(liste5)

liste6 = [f"le carrée de {x} est {x**2}" for x in liste]
print(liste6)

liste7 = [z * 10 for z in liste if z>2]
print(liste7)

liste8 = [w>3 for w in liste]
print(liste8)

liste9 = ['impair' if x%2 == 1 else x for x in liste]
print(liste9)

liste10 =[f"{x} est impair" if x%2==1 else f"{x} est pair" for x in liste]
print(liste10)