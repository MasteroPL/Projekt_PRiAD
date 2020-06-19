from Are_Rhymes import are_rhyming
import utils
import matplotlib.pyplot as plt
import numpy as np
from group_rhymes import RhymeGroup, RhymeGrouper

grupy = []
nazwa_pliku = 'Księgi Pana Tadeusza\\Księga{}.txt'
length = []
for x in range(1, 13):
    grouper = RhymeGrouper(are_rhyming)
    grouper.group(nazwa_pliku.format(x))
    grupy.append(grouper)
    length.append(len(open(nazwa_pliku.format(x), mode="r", encoding="utf-8"). readlines ()))

grouper1 = RhymeGrouper(are_rhyming)
grouper1.group('Księgi Pana Tadeusza\\Epilog.txt')
length.append(len(open('Księgi Pana Tadeusza\\Epilog.txt', mode="r", encoding="utf-8"). readlines ()))
grupy.append(grouper1)
grouper2 = RhymeGrouper(are_rhyming)
grouper2.group('Księgi Pana Tadeusza\\Pan Tadeusz Cały.txt')
grupy.append(grouper2)

evens = []
crosses = []
surrounding = []
unspecified = []


#colors [evens = green, surrounding = yellow, crossing = blue, unspecified = czerwone]

for x in range(13):
    evens.append(grupy[x].rhyme_groups["even"].__len__())
    crosses.append(grupy[x].rhyme_groups["cross"].__len__())
    surrounding.append(grupy[x].rhyme_groups["surrounding"].__len__())
    unspecified.append(grupy[x].rhyme_groups["unspecified"].__len__())
    

księgi = range(1,14)
księgin=np.array(księgi)

OX = np.array(księgi)
width = 0.2


plt.figure()

procent = []
for x in range(13):
    procent.append((evens[x]+crosses[x]+surrounding[x])/(length[x]/4))

plt.bar(OX, procent, label = 'procentowa zawartość rymów w tekście')
plt.title("Procentowa zawartość rymów w księgach")

plt.figure()


plt.bar(OX, surrounding[:13],width, label = 'okalające', color = "yellow")

plt.bar(OX, evens[:13], width, label = 'sasiadujace', bottom=surrounding[:13], color = "green")

suma = np.array(surrounding[:13]) + np.array(evens[:13])

plt.bar(OX,crosses[:13] ,width, label = 'krzyzowe', bottom = suma, color = "blue")

suma2 = suma + np.array(crosses[:13])

plt.bar(OX, unspecified[:13], width, label = 'nieokreślone', bottom=suma2, color = "red")

plt.legend(frameon=True,bbox_to_anchor=(1.05, 1))
plt.title("Ilość rymów w poszczególnych księgach")

plt.figure()

piechartx=[evens[-1],surrounding[-1],unspecified[-1],crosses[-1]]

plt.pie(piechartx, labels=["sasiadujace","okalające","nieokreślone", "krzyzowe"], colors=["green", "yellow","red","blue"])
plt.title("Procentowa zawartość rymów w Panu Tadeuszu")
plt.figure()

grouper3 = RhymeGrouper(are_rhyming)
grouper3.group('hymn.txt')
rymy = [grouper3.rhyme_groups["even"].__len__(), grouper3.rhyme_groups["cross"].__len__(), grouper3.rhyme_groups["unspecified"].__len__()]
xhymns = ["sąsiadujące","krzyżowe","okalające","nieokreślone"]
xh = np.array(xhymns)
plt.title("Procentowa zawartość rymów w wierszu \"Hymn\"")
plt.pie(rymy,labels = ["sąsiadujące","krzyżowe","nieokreślone"], colors=["green","blue","red"])

plt.figure()

grouper4 = RhymeGrouper(are_rhyming)
grouper4.group('DoTrupa.txt')
rymy2 = [grouper4.rhyme_groups["surrounding"].__len__(), grouper4.rhyme_groups["unspecified"].__len__()]
#,grouper4.rhyme_groups["even"].__len__(), grouper4.rhyme_groups["cross"].__len__()
plt.pie(rymy2,labels =["okalające","nieokreślone"] ,colors=["yellow","red"])
#,"sąsiadujące","krzyżowe"
plt.title("Procentowa zawartość rymów w wierszu \"Do Trupa\"")


plt.figure()

grouperMK = RhymeGrouper(are_rhyming)
grouperMK.group("Pan Balcer w Brazylii\sformatowane.txt")

piechartx=[grouperMK.rhyme_groups["even"].__len__(),grouperMK.rhyme_groups["cross"].__len__(),grouperMK.rhyme_groups["surrounding"].__len__(),grouperMK.rhyme_groups["unspecified"].__len__()]

plt.pie(piechartx, labels=["sasiadujace","krzyzowe","okalające","nieokreślone"], colors=["green","blue","yellow","red"])
plt.title("Procentowa zawartość rymów w \"Pan Balcer w Brazylii\"")

plt.show()