import os
import json

path = "spells_descriptions_new.txt"
final_array = []
tmp_array = {}

szkola = {
    "Iluzje",
    "Nekromancja",
    "Oczarowanie",
    "Odrzucanie",
    "Poznanie",
    "Przemiany",
    "Przywoływanie",
    "Wywoływanie"
}

okreslnik = {
    "chaos", 
    "ciemność", 
    "dobro", 
    "dźwięk", 
    "elektryczność", 
    "kwas", 
    "moc", 
    "ogień", 
    "oparty na języku", 
    "powietrze", "praworządność", 
    "śmierć", "strach", "światło", 
    "woda",
    "wpływający na umysł", 
    "ziemia", 
    "zimno", 
    "zło"
}


tmp_file = open(path, "r", encoding="utf-8")
all_lines = tmp_file.readlines()
print(all_lines[0])

with open(path,'r', encoding="utf-8") as file:
    for index,line in enumerate(file.readlines(), 1):
        NAZWA = ""
        SZKOLA = ""
        OKRESLNIK = ""
        POZIOM = ""
        KOMPONENTY = ""
        CZAS_RZUCANIA = ""
        ZASIEG = ""
        CELOWANIE_CZAREM = ""
        CZAS_DZIALANIA = ""
        RZUT_OBRONNY = ""
        ODPORNOSC_NA_CZARY = ""
        OPIS_DZIALANIA = ""

        if any(word in line for word in szkola): # linia ze szkola magii
            NAZWA = all_lines[index-1].strip()
            SZKOLA = line.strip()
            

            tmp_array = {
                "NAZWA":NAZWA,
                "SZKOLA":SZKOLA,
                "OKRESLNIK":OKRESLNIK,
                "POZIOM":POZIOM,
                "KOMPONENTY":KOMPONENTY,
                "CZAS_RZUCANIA":CZAS_RZUCANIA,
                "ZASIEG":ZASIEG,
                "CELOWANIE_CZAREM":CELOWANIE_CZAREM,
                "CZAS_DZIALANIA":CZAS_DZIALANIA,
                "RZUT_OBRONNY":RZUT_OBRONNY,
                "ODPORNOSC_NA_CZARY":ODPORNOSC_NA_CZARY,
                "OPIS_DZIALANIA":OPIS_DZIALANIA
            }

            final_array.append(tmp_array)


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