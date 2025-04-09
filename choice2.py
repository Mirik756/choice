import random
položka = ["obilí", "brambory", "rajčata", "papriky", "ořechy"]
for i in range (10):
    osoba1 = random.choice(položka)
    osoba2 = random.choice(položka)
    if osoba1 == osoba2:
        a = "jiné" + " "+ osoba2
    else:
        a = osoba2
    print(f"Kupme {osoba1}")
    print(f"ne, kupme {a}")