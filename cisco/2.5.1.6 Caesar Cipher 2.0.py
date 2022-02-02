def cipher(service, entrada, desloc):
    entrada = entrada.strip()
    saida = ''
    if service == 'code':
        for letter in entrada:
            if not letter.isalpha():
                saida += letter
                continue
            k = ord(letter) + desloc
            if 65 <= ord(letter) <= 90:
                if k <= 90:
                    saida += chr(k)
                else:
                    saida += chr(k - 26)             # 65 + k - 90 - 1
            else:
                if k <= 122:
                    saida += chr(k)
                else:
                    saida += chr(k - 26)             # 97 + k - 122 - 1
    if service == 'decode':
        for letter in entrada:
            if not letter.isalpha():
                saida += letter
                continue
            k = ord(letter) - desloc
            if 65 <= ord(letter) <= 90:
                if k >= 65:
                    saida += chr(k)
                else:
                    saida += chr(k + 26)              # 90 - (65 - k) + 1
            else:
                if k >= 97:
                    saida += chr(k)
                else:
                    saida += chr(k + 26)              # 122 - (97 - k) + 1
    return saida


while True:
    service = input('Digite "code" para codificar ou "decode" para decodificar: ').lower()
    if service == 'code' or 'decode':
        break
    else:
        print('Digite uma opção correta')
msg = input('Digite a mensagem: ')
deslocamento = 0
while True:
    deslocamento = input('Digite o deslocamento [1-25]: ')
    if not deslocamento.isdigit():
        print('Digite um número entre 1 e 25')
        continue
    if 1 <= int(deslocamento) <= 25:
        deslocamento = int(deslocamento)
        break
    else:
        print('Digite um número entre 1 e 25')

print(cipher(service, msg, deslocamento))
