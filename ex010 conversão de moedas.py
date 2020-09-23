real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.39
euro = real / 6.38
libra = real / 6.96
iene = real / 0.052
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${} você pode comprar €${:.2f}'.format(real, euro))
print('Com R${} você pode comprar £${:.2f}'.format(real, libra))
print('Com R${} você pode comprar ¥${:.2f}'.format(real, iene))


