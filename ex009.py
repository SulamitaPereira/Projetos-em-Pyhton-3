n1 = int(input('Digite a nota do 1° Bimestre '))
n2 = int(input('Digite a nota do 2° Bimestre '))
n3 = int(input('Digite a nota do 3° Bimestre '))
n4 = int(input('Digite a nota do 4° Bimestre '))
mf = ((n1+n2+n3+n4)/4)
if mf >= 5:
    print('Aprovado!')
else:
    print('Reprovado!')
