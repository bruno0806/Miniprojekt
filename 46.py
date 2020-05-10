import sys

elvalaszto = len(sys.argv) // 2 + 1
szamok = sys.argv[1: elvalaszto]
szamok = [int(i) for i in szamok]
jelek = sys.argv[elvalaszto:]

muvelet = ''
for i in range(elvalaszto - 2):
    muvelet += str(szamok[i]) + ' '
    muvelet += str(jelek[i]) + ' '
muvelet += str(szamok[elvalaszto - 2]) + ' '

i = 0
while i < len(jelek):
    if jelek[i] == '*':
        jelek.remove(jelek[i])
        ujszam = szamok[i] * szamok[i + 1]
        szamok[i] = ujszam
        szamok.remove(szamok[i + 1])
        i -= 1

    elif jelek[i] == '/':
        jelek.remove(jelek[i])
        ujszam = szamok[i] / szamok[i + 1]
        szamok[i] = ujszam
        szamok.remove(szamok[i + 1])
        i -= 1
    i += 1

i = 0
while i < len(jelek):
    jel = jelek.remove(jelek[i])
    if jel == '+':
        ujszam = szamok[i] + szamok[i + 1]
        szamok[i] = ujszam

    elif jel == '-':
        ujszam = szamok[i] - szamok[i + 1]
        szamok[i] = ujszam

    szamok.remove(szamok[i + 1])

muvelet += '= ' + str(szamok[0])
print(muvelet)
