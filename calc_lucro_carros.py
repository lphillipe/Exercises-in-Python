valor_pago = float(input('Valor pago: '))
valor_investido = float(input('Valor investido: '))
valor_venda = float(input('Valor da venda: '))

custo_total = valor_pago + valor_investido
lucro = valor_venda - custo_total

print('Custo total: R$ ' + str(custo_total))
print('Lucro obtido: R$' + str(lucro))

if lucro > 0:
    print('Resultado: Lucro na venda!')
elif lucro < 0:
    print('Resultado: Prejuizo na venda')
else:
    print('Resultado: Empate!')