# IBAN (International Bank Account Number) fornece um método simples e bastante fiável de validação dos números
# de conta contra erros de digitação simples. Um número de conta compatível com IBAN consiste em:
# um código de país de duas letras retirado da norma ISO 3166-1 (por exemplo, FR para a França, GB para a Grã-Bretanha,
# DE para a Alemanha, e assim por diante)
# dois dígitos de verificação utilizados para realizar as verificações de validade - testes rápidos e simples,
# mas não totalmente fiáveis, mostrando se um número é inválido (distorcido por uma gralha) ou se parece ser válido;
# o número real da conta (até 30 carateres alfanuméricos - o comprimento desta parte depende do país)
# versão simplificada

iban = input('Digite o IBAN: ').upper()
iban = iban.replace(' ', '')

if not iban.isalnum():
    print('Caracteres inválidos')
elif not 15 <= len(iban) <= 30:
    print('Tamanho incorreto')
else:
    iban = iban[4:] + iban[:4]
    iban2 = ''
    for i in iban:
        if i.isdigit():
            iban2 += i
        else:
            iban2 += str(ord(i) - 55)     # 55 = 10 - ord('A') = 10 - 65
    iban = int(iban2)
    if iban % 97 == 1:
        print('IBAN correto')
    else:
        print('IBAN incorreto')
