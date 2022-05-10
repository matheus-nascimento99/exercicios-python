#DESCONTO 5%
p = float(input('Qual o preço do produto?'))
d = p - (p * 0.05)

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, d))