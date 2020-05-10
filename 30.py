import numpy as np
import string

n = int(input("Adja meg a mátrix sorainak számát: "))
m = int(input("Adja meg a mátrix oszlopainak számát: "))
x = np.chararray((n, m), 1, True)
karakterek = np.array(list(string.ascii_lowercase))
matrix = np.random.choice(karakterek, [n, m])
keret = np.full((n + 2, m + 2), '*')

for i in range(n):
    for j in range(m):
        keret[i + 1][j + 1] = matrix[i][j]

print(keret)