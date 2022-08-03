path = "spells_descriptions.txt"

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
new_file = []

with open(path,'r', encoding="utf-8") as file:
    for index,line in enumerate(file.readlines(), 1):

        new_line = line
    
        if 0 <= index + 1 < len(all_lines):
            if any(word in all_lines[index + 1] for word in szkola):# linia ze szkola magii
                new_line = "\n"
                
        if line in ['\n', '\r\n']: # pusta linia
            new_line = ""

        new_file.append(new_line)


with open('spells_descriptions_new.txt', 'w', encoding="utf-8") as file_to_save:
    file_to_save.write(''.join(new_file))