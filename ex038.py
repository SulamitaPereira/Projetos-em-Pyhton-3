#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.        
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.       
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.   
print('*' *70)                                                                            
print('SEJA MUITO BEM-VINDO A NOSSA EMPRESA DE FINANCIAMENTOS!')                          
print('*' *50)                                                                            
print('Para iniciar o seu atendimento, por gentileza, insira seu nome abaixo:')           
nome = input(str('Primeiro nome: '))                                                      
sobrenome = input(str('Sobrenome: '))                                                     
print('Olá, {}! É um prazer ter você aqui conosco!' .format(nome))                        
print('Para seguirmos com a sua avaliação, preciso de algumas informações suas')          
valor = float(input('Insira aqui o valor do imóvel que deseja financiar: R$ '))           
print('Ok, o valor da casa é {}, e qual é o seu salário? (Renda líquida mensal)' .format(v
salario = float(input('O meu salário é de R$ '))                                          
print('Certo, já entendi! Agora me responda só mais uma coisa: Em quantos anos você preten
anos = int(input('Digite aqui o número de anos inteiros: '))                              
prestacao = valor / (anos * 12)                                                           
minimo = salario * 30 / 100                                                               
print('Para pagar uma casa de R${:.2f} em {} anos, ' .format(valor, anos), end='')        
print('a prestação será de R${:.2f}' .format(prestacao))                                  
if prestacao <= minimo:                                                                   
    print('O financiamento pode ser concedido!')                                          
else:                                                                                     
    print('Desculpe, mas não podemos te conceder o financiamento no momento :(')
