samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
sylaby = []
slowo = "Tadieusz"
niepodzielne = ("ch", "rz", "sz", "dz", "eu", "au")
inne = ("ą","ę","ć", "ś","ż", "ź", "ń", "ó")
laczniki = ("i",)


sylaba = ""
i = 0
while i < len(slowo):
    znak = slowo[i]
    byl_wyjatek = False

    # Wyszukiwanie wyjątków
    for wyjatek in niepodzielne:
        if len(wyjatek) <= len(slowo) - i:
            sub_str = slowo[i:(i+len(wyjatek)):1]
            if sub_str.upper() == wyjatek.upper():
                sylaba += wyjatek.upper()
                i += len(wyjatek) - 1
                byl_wyjatek = True

    if not byl_wyjatek:
        if znak in laczniki:
            sylaba += slowo[i:(i+2):1].upper()
            i += 1
            sylaby.append(sylaba)
            sylaba = ""
        elif znak in samogloski:
            sylaba += znak.upper()
            sylaby.append(sylaba)
            sylaba = ""
        else:
            sylaba += znak.upper()

    i += 1

if sylaba != "":
    sylaby.append(sylaba)

print(sylaby)