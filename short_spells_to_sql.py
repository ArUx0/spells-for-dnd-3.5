import os
import json

path_1 = "KLASY/"

classes = os.listdir(path_1)

final_array = []
tmp_array = {}

for clas in classes:
    path_2 = path_1+clas+"/"
    levels = os.listdir(path_2)
    for lvl in levels:
        path_3 = path_2+lvl
        CLASS = clas
        SPELL_LEVEL = lvl.rsplit(".", 1)[0]
        tmp_file = open(path_3, "r", encoding="utf-8")
        for line in tmp_file:
            line_tmp = line.split(":", 1)
            SPELL_NAME = line_tmp[0]
            SPELL_SHORT_DESCRIPTION = line_tmp[1].strip()
            tmp_array = {
                "CLASS":CLASS,
                "SPELL_LEVEL":SPELL_LEVEL,
                "SPELL_NAME":SPELL_NAME,
                "SPELL_SHORT_DESCRIPTION":SPELL_SHORT_DESCRIPTION,
            }
            final_array.append(tmp_array)
        tmp_file.close()


final_js_file = "data = '" + json.dumps(final_array) + "';"

final_js_file += "var spells_short = JSON.parse(data);"

with open('html/spells_short.js', 'w', encoding="utf-8") as spells_short:
    spells_short.write(final_js_file)


#df = pd.DataFrame([final_json])
#df.to_clipboard(index=False,header=False)
