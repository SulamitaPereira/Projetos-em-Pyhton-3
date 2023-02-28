oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print('O valor da hipotenusa: {:.2f}' . format(hipotenusa))

///

import math
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('O valor da hipotenusa: {:.2f}' . format(hipotenusa))

///

from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('O valor da hipotenusa: {:.2f}' . format(hipotenusa))
