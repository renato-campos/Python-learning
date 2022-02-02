# A sua tarefa é a de escrever um programa que seja capaz de simular o trabalho de um dispositivo de seven-display,
# embora vá utilizar LEDs individuais em vez de segmentos.
# Cada dígito é construído a partir de 13 LEDs (uns iluminados, outros escuros)
# O seu código tem de fazer um display de qualquer número inteiro não negativo inserido pelo utilizador.
#
# Dica: usar uma lista contendo padrões de todos os dez dígitos pode ser muito útil.

def display(number):
    number = str(number)
    std_display = [['###', '  #', '###', '###', '# #', '###', '###', '###', '###', '###'],
                   ['# #', '  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #'],
                   ['# #', '  #', '###', '###', '###', '###', '###', '  #', '###', '###'],
                   ['# #', '  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #'],
                   ['###', '  #', '###', '###', '  #', '###', '###', '  #', '###', '###']]
    for i in range(5):
        for n in number:
            print(std_display[i][int(n)], end=' ')
        print()



display(123)
display(9081726354)
