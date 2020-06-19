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
grupy.append(grouper1)
grouper2 = RhymeGrouper(are_rhyming)
grouper2.group('Księgi Pana Tadeusza\\Pan Tadeusz Cały.txt')
grupy.append(grouper2)

evens = []
crosses = []
surrounding = []
unspecified = []


for x in range(13):
    evens.append(grupy[x].rhyme_groups["even"].__len__())
    crosses.append(grupy[x].rhyme_groups["cross"].__len__())
    surrounding.append(grupy[x].rhyme_groups["surrounding"].__len__())
    unspecified.append(grupy[x].rhyme_groups["unspecified"].__len__())
    

księgi = range(1,13)
księgin=np.array(księgi)

OX = np.arange(len(księgi)) + 1
width = 0.2


plt.figure()




grouperMK = RhymeGrouper(are_rhyming)
grouperMK.group("Pan Balcer w Brazylii\sformatowane.txt")

piechartx=[grouperMK.rhyme_groups["even"].__len__(),grouperMK.rhyme_groups["cross"].__len__(),grouperMK.rhyme_groups["surrounding"].__len__(),grouperMK.rhyme_groups["unspecified"].__len__()]

plt.pie(piechartx, labels=["sasiadujace","krzyzowe","'okalające","nieokreślone"])


plt.figure()



procent = []
for x in range(12):
    procent.append((evens[x]+crosses[x]+surrounding[x])/(length[x]/4))



plt.bar(OX, procent, label = 'procentowa zawartość rymów w tekście')



plt.figure()
plt.bar(OX, surrounding[:12],width, label = 'okalające')

plt.bar(OX,crosses[:12] ,width, label = 'krzyzowe', bottom = surrounding[:12])

suma = np.array(surrounding[:12]) + np.array(crosses[:12])

plt.bar(OX, evens[:12], width, label = 'sasiadujace', bottom=suma)

suma2 = suma + np.array(evens[:12])

plt.bar(OX, unspecified[:12], width, label = 'nieokreślone', bottom=suma2)
plt.show()
plt.figure()
piechartx=[evens[-1],crosses[-1],surrounding[-1],unspecified[-1]]

plt.pie(piechartx, labels=["sasiadujace","krzyzowe","'okalające","nieokreślone"])

plt.figure()
grouper3 = RhymeGrouper(are_rhyming)
grouper3.group('hymn.txt')
rymy = [grouper3.rhyme_groups["even"].__len__(), grouper3.rhyme_groups["cross"].__len__(), grouper3.rhyme_groups["surrounding"].__len__(), grouper3.rhyme_groups["unspecified"].__len__()]
xhymns = ["sąsiadujące","krzyżowe","okalające","nieokreślone"]
xh = np.array(xhymns)
plt.bar(xh, rymy, width, label = 'hymn')

plt.figure()

grouper4 = RhymeGrouper(are_rhyming)
grouper4.group('DoTrupa.txt')
rymy2 = [grouper4.rhyme_groups["even"].__len__(), grouper4.rhyme_groups["cross"].__len__(), grouper4.rhyme_groups["surrounding"].__len__(), grouper4.rhyme_groups["unspecified"].__len__()]
plt.bar(xh, rymy2, width, label = 'Do Trupa')

plt.show()

print("Fuck Janek")