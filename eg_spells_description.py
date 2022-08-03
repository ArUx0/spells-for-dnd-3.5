import os
import json

path = "spells_descriptions_new.txt"
final_array = []
tmp_array = {}

szkola = {
    "Iluzje","Iluzja",
    "Nekromancja",
    "Oczarowanie", "Oczarowania",
    "Odrzucanie","Odrzucania",
    "Poznanie","Poznania",
    "Przemiany","Przemiana",
    "Przywoływanie","Przywoływania",
    "Wywoływanie","Wywoływania"
}

tmp_file = open(path, "r", encoding="utf-8")
all_lines = tmp_file.readlines()

NAZWA = ""
SZKOLA = ""
POZIOM = ""
KOMPONENTY = ""
CZAS_RZUCANIA = ""
ZASIEG = ""
OBSZAR = ""
CEL = ""
CELOWANIE_CZAREM = ""
CZAS_DZIALANIA = ""
RZUT_OBRONNY = ""
ODPORNOSC_NA_CZARY = ""
OPIS_DZIALANIA = ""

with open(path,'r', encoding="utf-8") as file:
    for index,line in enumerate(file.readlines(), 1):

        if line in ['\n', '\r\n']:
            tmp_array = {
                "NAZWA":NAZWA,
                "SZKOLA":SZKOLA,
                "POZIOM":POZIOM,
                "KOMPONENTY":KOMPONENTY,
                "CZAS_RZUCANIA":CZAS_RZUCANIA,
                "ZASIEG":ZASIEG,
                "OBSZAR":OBSZAR,
                "CEL":CEL,
                "CZAS_DZIALANIA":CZAS_DZIALANIA,
                "RZUT_OBRONNY":RZUT_OBRONNY,
                "ODPORNOSC_NA_CZARY":ODPORNOSC_NA_CZARY,
                "OPIS_DZIALANIA":OPIS_DZIALANIA
            }

            final_array.append(tmp_array)

            NAZWA = ""
            SZKOLA = ""
            POZIOM = ""
            KOMPONENTY = ""
            CZAS_RZUCANIA = ""
            ZASIEG = ""
            OBSZAR = ""
            CEL = ""
            CZAS_DZIALANIA = ""
            RZUT_OBRONNY = ""
            ODPORNOSC_NA_CZARY = ""
            OPIS_DZIALANIA = ""
            

        if any(word in line for word in szkola): # linia ze szkola magii
            if 0 <= index - 2 < len(all_lines):
                NAZWA = all_lines[index-2].strip()
            SZKOLA = line.strip()

        elif("Poziom:" in line):
            POZIOM = line.split(":", 1)[-1].strip()

        elif("Komponenty:" in line):
            KOMPONENTY = line.split(":", 1)[-1].strip()
        
        elif("Czas rzucania:" in line):
            CZAS_RZUCANIA = line.split(":", 1)[-1].strip()
        
        elif("Zasięg:" in line):
            ZASIEG = line.split(":", 1)[-1].strip()

        elif("Obszar:" in line):
            OBSZAR = line.split(":", 1)[-1].strip()

        elif("Cele:" in line or "Cel:" in line):
            CEL = line.split(":", 1)[-1].strip()

        elif("Czas działania:" in line):
            CZAS_DZIALANIA = line.split(":", 1)[-1].strip()

        elif("Rzut obronny:" in line):
            RZUT_OBRONNY = line.split(":", 1)[-1].strip()

        elif("Odporność na czary:" in line):
            ODPORNOSC_NA_CZARY = line.split(":", 1)[-1].strip()

        elif(NAZWA not in line):#("Opis" in line):
            OPIS_DZIALANIA += line.split(":", 1)[-1].strip()


final_js_file = "data = '" + json.dumps(final_array, ensure_ascii=False) + "';"
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

#NAZWA
#SZKOŁA (PODSZKOŁA)
#[OKREŚLNIK]
#POZIOM
#KOMPONENTY
#CZAS RZUCANIA
#ZASIĘG
#CELOWANIE CZAREM
#CZAS DZIAŁANIA
#RZUT OBRONNY
#ODPORNOŚĆ NA CZARY
#OPIS DZIAŁANIA