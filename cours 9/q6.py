virus_et_autres_info = [
    ["Virus-T", 0.9 ,"Transforme les humains en zombies et armes biologiques"],
    ["Virus-C", 0.0001 ,"Provoque des mutations extrêmes et régénère les tissus"],
    ["Virus-G", 0.85, "Cause des mutations incontrôlables avec régénération cellulaire rapide"],
    ["Uroboros", 0.005, "Consomme les organismes incompatibles et renforce les hôtes compatibles"]
]
print(f"Liste des {len(virus_et_autres_info)} virus :")
for v in virus_et_autres_info:
    print(f" {v[0]} - {v[2]} (taux de mutation estimé : {v[1] * 100}%)")