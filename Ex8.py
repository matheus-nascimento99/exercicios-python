n = int(input('Digite um número para ser sua tabuada: '))
print('------------------')
for i in range(0, 11):
    t = n*i
    print('{} x {} = {}'.format(n, i, t))
print('------------------')