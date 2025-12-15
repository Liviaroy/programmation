liste = [1, 2, 3, 4, 5]

cas1 = [x * 5 for x in liste]
print(cas1)

cas2 = [x + 3 for x in liste]
print(cas2)

cas3 = [x ** 2 for x in liste]
print(cas3)

cas4 = [str(x) for x in liste]
print(cas4)

cas5 = [x *2 for x in liste if x%2 == 0]
print(cas5)

cas6 = [f"Le carrée de {x} est {x**2}" for x in liste]
print(cas6)

cas7 = [x * 10 for x in liste if x > 2]
print(cas7)

cas8 = [x > 3 for x in liste]
print(cas8)

cas9 = ['impair' if x%2 == 1 else x for x in liste]
print(cas9)

cas10 = [f"{x} est impair" if x%2 == 1 else f"{x} est pair" for x in liste]
print(cas10)