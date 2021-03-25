#Jogo de adivinhação, o usuário precisa acertar o numério de 0 à 100 em no máximo 10 tentativas.
#Atividade da faculdade.
import random
numa = random.randint(0, 100)
print('-=-' * 10)
print('     JOGO DA ADIVINHAÇÃO')
print(' Adivinhe o número de 0 à 100')
print('-=-' * 10)
cont = 10
nIntNaoRepet = []
n = 0
maior = -1
menor = 101

while (cont != 0):
    print('\nTentativas restantes {}'.format(cont))
    n=int(input('Insirá um número: '))
    if n in nIntNaoRepet or n > 100:
        print('\nNuméro inválido, digite novamente!')
        continue
    else:
        cont -= 1
        nIntNaoRepet.append(n)
        if cont == 10:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        if n > numa:
            print('O n° digitado é maior que o número escondido.')
        elif n < numa:
            print('O n° digitado é menor que o número escondido')
        else:
            print('\n')
            print('-=-' * 10)
            print(' Parabéns. Você acertou!')
            break
else:
    print('-=-' * 10)
    print(' Você perdeu!')
    print(' O número escondido era {}'.format(numa))
print(' O maior valor da lista é {}'.format(maior))
print(' O menor valor da lista é {}'.format(menor))
print('-=-' * 10)
