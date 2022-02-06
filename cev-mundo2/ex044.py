price = float(input('Preço das compras: R$'))
forma_pag = input('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/débito/Pix
[2] à vista crédito
[3] 2x no cartão
[4] 3x ou mais no cartão
qual sua opção? -> ''')
if forma_pag == '1':
    print(f'\nSua compra de R${price:.2f} sairá à vista por R${price*0.9:.2f}')
elif forma_pag == '2':
    print(f'\nSua Compra de {price:.2f} sairá à vista no crédito por R${price*0.95:.2f}')
elif forma_pag == '3':
    print(f'''\nSua compra de R${price:.2f}
terá 2 parcelas de R${price/2:.2f} no cartão
totalizando R${price:.2f}''')
elif forma_pag == '4':
    parc = int(input('Quantas parcelas: '))
    print(f'''\nSua compra de R${price:.2f}
terá {parc} parcelas de R${price*1.2/parc} no cartão
totalizando R${price*1.2}''')
else:
    print('Opção de forma de pagamento inválida.')
