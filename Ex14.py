d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

valordias = d * 60
valorkm = km * 0.15
valortotal = valordias + valorkm

print('O total a pagar é de R${}'.format(valortotal))
