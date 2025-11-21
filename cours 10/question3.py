info = {
    "lieu": "Raccon City",
    "date": "2025-07-12",
    "temperatures_C": {
        "matin": 18.2,
        "midi": 22.5,
        "apres_midi": 24.1,
        "soir": 20.3
    }
}

date = info["date"]
print(f"Températures à Raccon City le {date}")
print()

temperatures_matin = info["temperatures_C"]["matin"]
temperatures_midi = info["temperatures_C"]["midi"]
temperatures_apres = info["temperatures_C"]["apres_midi"]
temperatures_soir = info["temperatures_C"]["soir"]

print(f"  Matin       : {temperatures_matin} C")
print(f"  Midi        : {temperatures_midi} C")
print(f"  Après-midi  : {temperatures_apres} C")
print(f"  Soir        : {temperatures_soir} C")
print()

moyenne = (info["temperatures_C"]["matin"] + info["temperatures_C"]["midi"]+info["temperatures_C"]["apres_midi"]+info["temperatures_C"]["soir"])/4
moyenne_arondie = round(moyenne, 2)
print(f"Température moyenne : {moyenne_arondie} C")



"""
Températures à Raccon City le 2025-07-12

  Matin       : 18.2 °C
  Midi        : 22.5 °C
  Après-midi  : 24.1 °C
  Soir        : 20.3 °C

Température moyenne : 21.28 °C

"""