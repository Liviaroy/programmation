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
print(f"Températures à Raccon City le {info['date']}")
temp_matin = info["temperatures_C"]["matin"]
temp_midi = info["temperatures_C"]["midi"]
temp_pm = info["temperatures_C"]["apres_midi"]
temp_soir = info["temperatures_C"]["soir"]
print()
print(f"Matin       : {temp_matin}°C")
print(f"Midi        : {temp_midi}°C")
print(f"Après-midi  : {temp_pm}°C")
print(f"Soir        : {temp_soir}°C")
print()
temperature_moy = (temp_matin + temp_midi + temp_pm + temp_soir)/4
temp_arondie = round(temperature_moy, 2)
print(f"Température moyenne : {temp_arondie}°C")
"""Températures à Raccon City le 2025-07-12

  Matin       : 18.2 °C
  Midi        : 22.5 °C
  Après-midi  : 24.1 °C
  Soir        : 20.3 °C

Température moyenne : 21.28 °C"""