somme = 0
z = 0

with open("temperatures.txt", "r") as f:
     for ligne in f:
         temps = float(ligne)
         somme += temps
         z += 1
         moyenne = somme / z
         print(moyenne)
         

