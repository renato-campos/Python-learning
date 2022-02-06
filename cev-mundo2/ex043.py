peso = float(input('Qual o seu peso em kg: '))
altura = float(input('Qual a sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif imc < 25:
    status = 'com PESO IDEAL'
elif imc < 30:
    status = 'com SOBREPESO'
elif imc < 40:
    status = 'com OBESIDADE'
else:   # imc >= 40
    status = 'com OBESIDADE MÓRBIDA'

print(f'''O IMC da pessoa é {imc:.1f}
Ela está {status}''')
