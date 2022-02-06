# entrada de dados
valor_casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual seu salário: R$'))
tempo = int(input('Quantos anos para pagar: '))
# cálculo da prestação do financiamento
prestacao = valor_casa / (tempo * 12)
# decisão e resultado
if prestacao <= 0.3 * salario:
    print(f'\nO valor da prestação será de R${prestacao:.2f}\nFinanciamento \033[1;32mAprovado\033[m')
else:
    print('\nA prestação excedeu o limite.\nFinanciamento \033[1;31mNegado\033[m')
