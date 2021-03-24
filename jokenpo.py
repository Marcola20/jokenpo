#Jokenpô desenvolvido por Marcos Vinicius
#versão 2.1

from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura', 'NADA', 'NADA', 'NADA')
cpu = randint(0, 2)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('''Olá, iremos jogar Jokênpo.
Quem fizer três pontos primeiro vence!''')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sleep(1)

jog = 0
pc = 0
while (jog < 3 and pc < 3):
    print('''\n-=-=-=- JOKENPÔ -=-=-=-
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    j = int(input('Qual é sua jogada? '))
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    sleep(1)
    print('         JO')
    sleep(1)
    print('        KEEN')
    sleep(1)
    print('         PÔ')
    sleep(1)
    print('O computador jogou {}'.format(itens[cpu]))
    print('O jogador jogou {}'.format(itens[j]))
    print('-=-=-=-=-=-=-=-=-=-=-=-')

    if cpu == 0: #Pedra
        if j == 0: #Pedra
            print('Empate!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 1: #Papel
            print(''' PAPEL EMBRULHA PEDRA!
 JOGADOR VENCEU!!''''')
            jog += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 2: #Tesoura
            print(''' PEDRA QUEBRA TESOURA! 
 COMPUTADOR VENCEU!!''')
            pc += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j > 2:
            print('JOGADA INVÁLIDA!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
            continue
            print('\n')
        sleep(1)

    elif cpu == 1: #Papel
        if j == 0:  #Pedra
            print(''' PAPEL EMBRULHA PEDRA!
 COMPUTADOR VENCEU!!''')
            pc += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 1:  #Papel
            print('Empate!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 2:  #Tesoura
            print(''' TESOURA CORTA PAPEL!
 JOGADOR VENCEU!!''')
            jog += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j > 2:
            print('JOGADA INVÁLIDA!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
            print('\n')
            continue
        sleep(1)

    elif cpu == 2: #Tesoura
        if j == 0:  #Pedra
            print(''' PEDRA QUEBRA TESOURA! 
 JOGADOR VENCEU!!''')
            jog += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 1:  #Papel
            print(''' TESOURA CORTA PAPEL!
 COMPUTADOR VENCEU!!''')
            pc += 1
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j == 2:  #Tesoura
            print('Empate!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
        elif j > 2:
            print('JOGADA INVÁLIDA!')
            print('-=-=-=-=-=-=-=-=-=-=-=-')
            print('\n')
            continue
        sleep(1)

if jog == 3:
    print('PARABÉNS. Você venceu o Computador!')
elif pc == 3:
    print('VISH. O Computador foi o vencedor!')

