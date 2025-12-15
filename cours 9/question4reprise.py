import random

nombre_secret = random.randint(1, 100)
essais = []
essai = int(input(f" Tente de trouver le nombre que j'ai en tête : "))
trouve = False
while not trouve :

    essai = int(input(f" Tente de trouver le nombre que j'ai en tête : "))

    if essai in essais :
        print("Pas le seven-up le plus petillant de la caisse boboy!!")
        essais.append(essai)
    if essai == nombre_secret:
        print(f"Bravo humain, tu as trouvé le nombre!")
        trouve = True
    elif essai > nombre_secret:
        print(f"Plus bas!")
    else :
        print(f"Plus haut!")

