velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! VOCÊ EXCEDEU O LIMITE DE VELOCIDADE PERMITIDO QUE É 80KM/H')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!' .format(multa))
print('Tenha um bom dia, dirija com segurança!')
