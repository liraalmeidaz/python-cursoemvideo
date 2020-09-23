preco = float(input('Qual é o salário do Funcionário? R$'))
novo = preco + (preco * 15 / 100)
print('O produto que custava R${:.2f}, na promoção de 5% custará: R${:.2f} '.format(preco, novo))
