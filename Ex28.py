import random
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
palpite = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
if(palpite == escolhido):
    print('PARABÉNS! Você me venceu! ')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(escolhido, palpite))