import matplotlib.pyplot as plt

plt.title('Dropout (dev Set)')
plt.xlabel('epochs')
plt.ylabel('loss')
x = list(range(0, 20))
plt.xticks(range(20))
# dropout train
# y_1 = [0.4729546694556872, 0.29047081179420153, 0.1548648795162638, 0.08616125836595893, 0.04082513275525222, 0.03157019376878937, 0.027457111032834897, 0.04754340441946018, 0.04878046712574238, 0.04767194148511529, 0.023224238897688338, 0.01785810906486828, 0.02380384257642436, 0.01730847427060856, 0.014585194264119005, 0.027137772515317467, 0.04265419103733469, 0.029817311499465822, 0.01740948211064178, 0.02371892991314909]
# y_2 = [0.4672506800691287, 0.30460464693109196, 0.20534144921104114, 0.13253187978019318, 0.08221637226951618, 0.05296635346673429, 0.051709019334676365, 0.044266238934903716, 0.042167728710880814, 0.053292204200522976, 0.04543412213617315, 0.034281177967864396, 0.04076754716356785, 0.03343840687461367, 0.03357638735693763, 0.04354287026751505, 0.03212924781010224, 0.031058798939045423, 0.02734553083971847, 0.031438479687235336]
# y_3 = [0.48934612472852074, 0.3439071738322576, 0.26152499111990135, 0.1857134166409572, 0.1333300338163972, 0.10714206577464938, 0.09317040357987086, 0.07136234903894365, 0.06861766491807066, 0.0540830387774234, 0.06643375454672301, 0.054255874445196244, 0.04531157457724718, 0.03876389612942391, 0.041977736880927596, 0.04290178747385653, 0.04347763712116739, 0.04791569590011568, 0.07442814573261906, 0.04650759351796448]
# y_4 = [0.517284984588623, 0.3796389740506808, 0.31134191633264224, 0.24892983460923035, 0.21087342206637064, 0.16761469937612614, 0.14142517158513268, 0.125570325360323, 0.11690919497112433, 0.09372207999384652, 0.09462263672240079, 0.0952354308248808, 0.08381047807106128, 0.08396161559747997, 0.06527341489175645, 0.08092561194372926, 0.07439928390274872, 0.07254326398459185, 0.06379768931566893, 0.05324645790677945]
# y_5 = [0.5430641798575719, 0.4260705807407697, 0.36302156492074333, 0.3244356335202853, 0.2943493513067563, 0.27637065648039183, 0.23034343122442563, 0.20427160293857258, 0.18004463900936146, 0.1937000040151179, 0.16606747348358233, 0.1474113267424206, 0.14385536077059805, 0.12916646234598012, 0.13559909785135338, 0.1122082875839745, 0.12242336461592156, 0.11587949462219452, 0.11272956720863779, 0.10376132758186819]
# y_6 = [[1.1527596331646828, 1.0458037733795151, 0.3664627551795944, 0.42353754141737543, 0.516840580082129]]
# learning rate train
# y_1 = [1.440807976519068, 1.0338448156652351, 0.9539522092603147, 0.7461350376078238, 0.527601817852507, 0.5346065649836867, 0.5474442004264759, 0.4009908467172839, 0.521563679537115, 0.6027770689330114, 0.5945139984650402, 0.5118341554786049, 0.5874175029014562, 0.5009242311688905, 0.4917443695608404, 0.6687847045390742, 0.5316370639153465, 0.4994651400896361, 0.500929971866783, 0.5333053372760196]
# y_2 = [0.40040742115940275, 0.4060120001869121, 0.23170081664260941, 0.2600333928838718, 0.2699344387123128, 0.22479711629441773, 0.28865674732057384, 0.2216883948255994, 0.2756186432320389, 0.20623750515844463, 0.2097794627847846, 0.17452111301828716, 0.2042361866547162, 0.18960427979733166, 0.19814928385615174, 0.2950711688879577, 0.25649458312218243, 0.28111670534985295, 0.27921605512120734, 0.19081596120125288]
# y_3 = [0.28483943843034404, 0.22932711425986296, 0.1911991573323806, 0.16793184494242694, 0.16081923074989268, 0.1424699887894094, 0.13961697288556024, 0.12776978615857662, 0.1365569770738172, 0.1426583430309159, 0.13124036411731504, 0.11224541768905086, 0.11922887932322919, 0.1015124823381775, 0.1115876011485622, 0.09923723502177745, 0.10374492735710616, 0.09661697956830419, 0.11793590208662984, 0.09419828050537035]
# y_4 = [0.13386187592304002, 0.11791010478352351, 0.11976939704516554, 0.11680696790211369, 0.11552774875692558, 0.10256661104643718, 0.11294056452237419, 0.10752200601819398, 0.10943042097465756, 0.10375391460503064, 0.10622880367795005, 0.10393221046185742, 0.09541442024397354, 0.09354168684221804, 0.09439519309050715, 0.08556342146134314, 0.09196599518701745, 0.09337420817945774, 0.09672630784182912, 0.09053591320541454]
# y_5 = [0.11144513906817884, 0.10646346384348969, 0.09970811736131631, 0.11074730112341544, 0.12219008936709724, 0.1084618839812465, 0.10526501961972098, 0.0911898111901246, 0.10771627126055924, 0.10826084599892298, 0.1174802928014736, 0.09998068968586935, 0.10662580447488774, 0.10629334796642555, 0.10095675167371519, 0.09007611060406392, 0.09892989061683571, 0.09598090393693808, 0.10574054871546104, 0.1001148541687628]
# learning rate dev
y_1 = []
y_2 = []
y_3 = []
y_4 = []
y_5 = []
# y_1 = []
# y_2 = []
# y_3 = []
# y_4 = []
# y_5 = []
# y_1 = []
# y_2 = []
# y_3 = []
# y_4 = []
# y_5 = []
# y_5 = []
plt.plot(x, y_1, label='0.1')
plt.plot(x, y_2, label='0.2')
plt.plot(x, y_3, label='0.3')
plt.plot(x, y_4, label='0.4')
plt.plot(x, y_5, label='0.5')
# plt.plot(x, y_6)
plt.legend(loc="best")
plt.show()

# prop设置字体，目标是支持中文