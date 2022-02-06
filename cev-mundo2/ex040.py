# ENTRADA DE NOTAS
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
# CÁLCULO DA MÉDIA
media = (nota1 + nota2) / 2
if media >= 7:
    situacao = '\033[1;32mAPROVADO\033[m'
elif 5 <= media < 7:
    situacao = '\033[1;33mRECUPERAÇÃO\033[m'
else:       # media < 5
    situacao = '\033[1;31mREPROVADO\033[m'
# RESULTADO
print(f'''Com as notas {nota1} e {nota2} a média é {media}
O aluno está {situacao}''')