from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é a sua jogada?:'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)
print('-=' *10)
print(f'O computador escolheu: {itens[computador]}')
print(f'O jogador escolheu: {itens[jogada]}')
print('-=' *10)


if computador == 0:
    if jogada == 0:
        print('Empate')
    elif jogada == 1:
        print('Jogador VENCEU!')
    elif jogada == 2:
        print('Computatdor VENCEU!')
    else:
        print('Jogada invalida')

elif computador == 1:
    if jogada == 0:
        print('Computador VENCEU')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('Jogador VENCEU')
    else:
        print('Jogada invalida')

elif computador == 2:
    if jogada == 0:
        print('Jogador VENCEU!')
    elif jogada == 1:
        print('Computador VENCEU!')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('Jogada Invalida')