import math
ang = float(input('Qual é o ângulo? '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians (ang))
tangente = math.tan(math.radians (ang))
print ('O ÂNGULO tem o seno de {:.2f}\nO COSSENO de {:.2f} \nE a TANGENTE de {:.2f}' .format(seno, cosseno, tangente))

///

import math
ang = float(input('Digite o valor do ângulo: ')
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print ('O ângulo tem o SENO de {:.2f}' .format(seno))
print ('O COSSENO de {:.2f}' .format(cosseno))
print ('E a TANGENTE de {:.2f}' .format(tangente))

///

from math import radians, sin, cos, tan
ang = float(input('Digite o valor do ângulo: ')
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print ('O ângulo tem o SENO de {:.2f}' .format(seno))
print ('O COSSENO de {:.2f}' .format(cosseno))
print ('E a TANGENTE de {:.2f}' .format(tangente))
