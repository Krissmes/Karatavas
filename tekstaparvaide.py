with open("word_list.py","r", encoding="utf-8") as f:
    saturs = f.readlines()
    jaunais = [saturs[0]]
    for rinda in saturs[1:]:
        rinda = rinda.strip("\n")
        rakstamais = "\'" + rinda + "\', \n"
        jaunais.append(rakstamais)

with open("word_list.py","w", encoding="utf-8") as f:
    f.write("".join(jaunais))