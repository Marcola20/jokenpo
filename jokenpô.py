#Jokenpô desenvolvido por Marcos Vinicius
#versão 1.0

from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('''Olá, iremos jogar Jokênpo.
Quem fizer três pontos primeiro vence!''')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sleep(2)

jog = 0
pc = 0
while (jog < 3 and pc < 3):
    print('''-=-=-=- JOKENPÔ -=-=-=-
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    j = int(input('Qual é sua jogada? '))
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    print('O computador jogou {}'.format(itens[cpu]))
    print('O jogador jogou {}'.format(itens[j]))
    print('-=-=-=-=-=-=-=-=-=-=-=-')

    if cpu == 0: #Pedra
        if j == 0: #Pedra
            print('Empate!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 1: #Papel
            print('JOGADOR VENCEU!!')
            jog += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 2: #Tesoura
            print('COMPUTADOR VENCEU!!!')
            pc += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        else:
            print('JOGADA INVÁLIDA!')
        sleep(2)

    elif cpu == 1: #Papel
        if j == 0:  #Pedra
            print('COMPUTADOR VENCEU!!')
            pc += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 1:  #Papel
            print('Empate!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 2:  #Tesoura
            print('JOGADOR VENCEU!!')
            jog += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        else:
            print('JOGADA INVÁLIDA!')
        sleep(2)

    elif cpu == 2: #Tesoura
        if j == 0:  #Pedra
            print('JOGADOR VENCEU!!')
            jog += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 1:  #Papel
            print('COMPUTADOR VENCEU!!')
            pc += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 2:  #Tesoura
            print('Empate!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        else:
            print('JOGADA INVÁLIDA!')
        sleep(2)

if jog == 3:
    print('PARABÉNS. Você venceu o Computador!')
elif pc == 3:
    print('VISH. O Computador foi o vencedor!')

