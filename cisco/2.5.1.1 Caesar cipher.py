# Caesar Cipher: cada letra da mensagem é substituída pela sua consequente mais próxima (A torna-se B, B torna-se C,
# e assim por diante). A única exceção é Z, que se torna A. Escrevemo-lo utilizando os seguintes pressupostos:
#
# aceita apenas letras latinas (nota: os romanos não usavam espaços em branco nem dígitos)
# todas as letras da mensagem estão em maiúsculas (nota: os romanos conheciam apenas maiúsculas)

def cipher(msg):
    msg = msg.strip().upper()
    code = ''
    for letter in msg:
        if 65 <= ord(letter) < 90:
            code += chr(ord(letter) + 1)
        elif ord(letter) == 90:
            code += 'A'
        else:
            return 'Você usou caracteres não suportados.'
    return code


def decipher(code):
    code = code.strip().upper()
    msg = ''
    for letter in code:
        if 90 >= ord(letter) > 65:
            msg += chr(ord(letter) - 1)
        elif ord(letter) == 65:
            msg += 'Z'
        else:
            return 'Você usou caracteres não suportados.'
    return msg


msg = input('Digite a mensagem a codificar: ')
print('Mensagem codificada: ', cipher(msg))

codigo = input('Digite o código a decifrar: ')
print('Mensagem decifrada: ', decipher(codigo))
