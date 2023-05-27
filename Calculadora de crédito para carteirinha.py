from math import floor
from time import sleep
print('----------Calculadora de Carteirinha-----------')
print('''Escolha o seu tipo de carteirinha:
[ 1 ] Carteirinha Estundantil (R$ 2,25)
[ 2 ] Carteirinha Passe Livre (R$ 4,50)''')
op = int(input('Opção: '))
valor = float(input('Quanto você irá colocar na carteirinha: R$'))
dias = int(input('Quantos dias a carteirinha deve durá: '))
passagens = int(input('Quantas passagens você usa por dia: '))

if op == 1:
    valorPDias = passagens * 2.25
    valorDias = valor / valorPDias
    print('CALCULANDO !!!')
    sleep(2)
    print('De acordo com o valor escolhido, os créditos irá durar por {} dias'.format(floor(valorDias)))
    if valorDias < dias:
        total_passagens = dias * passagens
        total_necessario = 2.25 * total_passagens
        falta_dinheiro = total_necessario - valor
        print('Falta R$ {:.2f} reais para {} dias'.format(falta_dinheiro, dias))

elif op == 2:
    valorPDias = passagens * 4.50
    valorDias = valor / valorPDias
    print('CALCULANDO !!!')
    sleep(2)
    print('De acordo com o valor escolhido, os créditos irá durar por {} dias'.format(floor(valorDias)))
    if valorDias < dias:
        total_passagens = dias * passagens
        total_necessario = 4.50 * total_passagens
        falta_dinheiro = total_necessario - valor
        print('Falta R$ {:.2f} reais para {} dias'.format(falta_dinheiro, dias))
