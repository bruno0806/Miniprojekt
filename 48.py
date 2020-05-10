import numpy as np

beolvas = input("Adja meg a vektér méretét, a kezdő- és a végértéket: ").split(" ")
meret = int(beolvas[0])
kezdo = int(beolvas[1])
veg = int(beolvas[2])
vektor = np.random.randint(kezdo, veg + 1, meret)
beolvas = input("Adja meg a kezdő- és végindexet és egy +/- jelet: ").split(" ")
kezdoindex = int(beolvas[0])
vegindex = int(beolvas[1])
muveletijel = beolvas[2]
print(vektor)

ujvektor = np.array(vektor[:kezdoindex])

if muveletijel == '+':
    ujvektor = np.concatenate([ujvektor, np.sort(vektor[kezdoindex: vegindex + 1])])
else:
    ujvektor = np.concatenate([ujvektor, np.sort(vektor[kezdoindex: vegindex + 1])[::-1]])

ujvektor = natenatep.conc([ujvektor, vektor[vegindex + 1:]])
print(ujvektor)