from math import floor
from time import sleep
print('-=-=-=-=-=-=-=-=-=-=-=- CALCULADORA DE CARTEIRINHA -=-=-=-=-=-=-=-=-=-=-=-=-')
print('''Escolha as opções:
[ 1 ] Carteirinha Estundantil (R$ 2.25)
[ 2 ] Vale Transporte (R$ 4.50)
[ 3 ] Quantas dias acaba a passagem  (OBS: Lembrando que você precisar saber quanto tem no seu vale transporte)
[ 4 ] Quanto eu preciso recarregar? 
OBS: Por favor utilize "."(ponto) em vez de ","(vírgula). Obrigado ''')
op = int(input('Opção: '))

if op == 1:
    print('-='*20)
    valor = float(input('Quanto você irá colocar na carteirinha: R$'))
    dias = int(input('Quantos dias a carteirinha deve durá: '))
    passagens = int(input('Quantas passagens você usa por dia: '))
    valorPDias = passagens * 2.25
    valorDias = valor / valorPDias
    print('-='*20)
    print('CALCULANDO !!!')
    print('-=' * 20)
    sleep(2)
    print('De acordo com o valor escolhido, os créditos irá durar por {} dias'.format(floor(valorDias)))
    if valorDias < dias:
        total_passagens = dias * passagens
        total_necessario = 2.25 * total_passagens
        falta_dinheiro = total_necessario - valor
        print('Falta R$ {:.2f} reais para {} dias'.format(falta_dinheiro, dias))

elif op == 2:
    valor = float(input('Quanto você irá colocar na carteirinha: R$'))
    dias = int(input('Quantos dias a carteirinha deve durá: '))
    passagens = int(input('Quantas passagens você usa por dia: '))
    valorPDias = passagens * 4.50
    valorDias = valor / valorPDias
    print('-='*20)
    print('CALCULANDO !!!')
    print('-=' * 20)
    sleep(2)
    print('De acordo com o valor escolhido, os créditos irá durar por {} dias'.format(floor(valorDias)))
    if valorDias < dias:
        total_passagens = dias * passagens
        total_necessario = 4.50 * total_passagens
        falta_dinheiro = total_necessario - valor
        print('Falta R$ {:.2f} reais para {} dias'.format(falta_dinheiro, dias))

elif op == 3:
    print('''Qual a sua carteirinha?
        [ 1 ] Carteirinha Estudantil
        [ 2 ] Vale transporte
        ''')
    op = int(input('Opção: '))
    valorCarteirinha = float(input('Quanto tem no seu vale transporte: R$'))
    passagens = int(input('Quantas passagens você usa por dia? '))

    if op == 1:
        valorPDias = passagens * 2.25
        valorDias = valorCarteirinha / valorPDias
        print('-='*20)
        print('CALCULANDO !!!')
        print('-=' * 20)
        sleep(2)
        print('De acordo com o valor que você possui, tem R${:.2f} na carteirinha estundantil que dá por {} dia.'.format(valorCarteirinha, floor(valorDias)))

    elif op == 2:
        valorPDias = passagens * 4.50
        valorDias = valorCarteirinha / valorPDias
        print('-='*20)
        print('CALCULANDO !!!')
        print('-=' * 20)
        sleep(2)
        print('De acordo com o valor que você possui, tem R${:.2f} no vale transporte que dá por {} dias.'.format(valorCarteirinha, floor(valorDias)))

elif op == 4:
    print('''Qual o seu tipo de vale transporte?
    [ 1 ] Carteirinha Estudantil
    [ 2 ] Vale transporte''')
    op = int(input('Qual opção: '))
    dias = int(input('Quantas dias será utilizado do vale transporte? '))
    passagens = int(input('Quantas vezes por dia você utiliza o vale transporte? '))

    if op == 1:
        valorPDias = passagens * 2.25
        valorTotal = valorPDias * dias
        print('-=' * 20)
        print('CALCULANDO !!!')
        print('-=' * 20)
        sleep(2)
        print('\nVocê irá precisar fazer uma recarga de R${:.2f} para a quantidade de dias que você necessita.'.format(valorTotal))

    elif op == 2:
        valorPDias = passagens * 4.50
        valorTotal = valorPDias * dias
        print('-=' * 20)
        print('CALCULANDO !!!')
        print('-=' * 20)
        sleep(2)
        print('\nVocê irá precisar fazer uma recarga de R${:.2f} para a quantidade de dias que você necessita.'.format(valorTotal))

