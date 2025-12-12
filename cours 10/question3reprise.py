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
"""Températures à Raccon City le 2025-07-12

  Matin       : 18.2 °C
  Midi        : 22.5 °C
  Après-midi  : 24.1 °C
  Soir        : 20.3 °C

Température moyenne : 21.28 °C"""

temperatures = info['temperatures_C']
#print(temperatures)
#print(temperatures['matin'])
#print(temperatures['midi'])

moyenne = (temperatures['soir'] + temperatures["matin"] + temperatures["midi"] + temperatures["apres_midi"]) / 4
moyenne_arondie = round(moyenne, 2)

print(f"Températures à Raccon City le {info['date']}")
print()
print(f"Matin       : {temperatures['matin']}°C")
print(f"Midi        : {temperatures["midi"]}°C")
print(f"Après-midi  : {temperatures["apres_midi"]}°C")
print(f"Soir        : {temperatures["soir"]}°C")
print()
print(f"Températures moyenne : {moyenne_arondie}")