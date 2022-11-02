txt = "Hugo zjedol dedov syr."
f1, f2, t1, t2 = open("uloha3_1.txt", "w"), open("uloha3_2.txt", "w"), " ".join([char for char in txt[::2]]), " ".join([char for char in txt[1::2]])
[f1.write(t1)] + [f2.write(t2)]