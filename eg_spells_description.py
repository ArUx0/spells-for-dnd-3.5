import os
import json

path = "spells_descriptions.txt"
final_array = []
tmp_array = {}

tmp_file = open(path, "r", encoding="utf-8")
for line in tmp_file:
    NAME = line;
    DOMAIN = line;
    tmp_array = {
        "NAME":NAME,
        "DOMAIN":DOMAIN,
    }
    final_array.append(tmp_array)
tmp_file.close()


final_js_file = "data = '" + json.dumps(final_array) + "';"

final_js_file += "var spells_long = JSON.parse(data);"

with open('html/spells_long.js', 'w', encoding="utf-8") as spells_short:
    spells_short.write(final_js_file)


#df = pd.DataFrame([final_json])
#df.to_clipboard(index=False,header=False)

#Alarm
#Odrzucanie
#Poziom: Brd 1, Cza/Zak 1, Trp 1
#Komponenty: W, S, K/KO
#Czas rzucania: 1 akcja standardowa
#Zasięg: Bliski (7,5 m + 1,5 m/2 poziomy)
#Obszar: Emanacja o promieniu 6 metrów i środku w jakimś punkcie przestrzeni
#Czas działania: 2 godziny/poziom (P)
#Rzut obronny: Brak
#Odporność na czary: Nie