d = float(input('Por quantos dias o carro foi alugado? '))
k = float(input('Quantos quilômetros foram percorridos? '))
d1 = d * 60
k1 = k * 0.15
t = d1 + k1
print ('O valor total a pagar pelo aluguel é de: R$ {:.2f}!' .format(t))
