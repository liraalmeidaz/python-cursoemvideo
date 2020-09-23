salario = float(input('Qual é o salario do Funcionário R$ '))
novo = salario + (salario * 15 / 100)
print('O funcionário que recebia R${:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(salario, novo))