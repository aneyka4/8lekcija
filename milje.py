# -*- coding: utf-8 -*-
print("Živijo! S tem pregramom se pretvarjajo kilometri v milje!")

while True:
    num = int(raw_input("Vnesi število kilometrov: "))
    km = str(num*0.62)
    print("Odgovor je " + km + " milj.")
    vpr = (raw_input("Če želite nadaljevati vtipkajte DA, če želite končati vtipkajte NE"))
    if vpr == "da":
        continue
    if vpr == "ne":
        print("Hvala in nasvidenje!")
        break7
        7