# A sua tarefa é escrever a sua própria função, que se comporta quase exatamente como o método original split() , ou seja:
#
# deve aceitar exatamente um argumento - uma string;
# deve devolver uma lista de palavras criadas a partir da string, dividida nos locais onde a string contém espaços em branco;
# se a string estiver vazia, a função deve devolver uma lista vazia;
# o seu nome deve ser mysplit()

def mysplit(msg):
    msg = msg.strip()
    if msg == '':
        return []
    lista = []
    k = 1
    while k != -1:
        k = msg.rfind(' ')
        lista.insert(0, msg[k+1:])
        msg = msg[:k]
    return lista


def mysplit2(msg):
    if msg == '' or msg.isspace():      # return [] if string is empty or contains whitespaces only
        return [ ]
    lista = []                          # prepare a list to return
    word = ''                           # prepare a word to build subsequent words
    inword = not msg[0].isspace()       # check if we are currently inside a word (i.e., if the string starts with a word)
    for x in msg:                       # iterate through all the characters in string
        if inword:                      # if we are currently inside a string...
            if not x.isspace():         # ... and current character is not a space...
                word = word + x         # ... update current word
            else:
                lista.append(word)      # ... otherwise, we reached the end of the word so we need to append it to the list...
                inword = False          # ... and signal a fact that we are outside the word now
        else:

            if not x.isspace():         # if we are outside the word and we reached a non-white character...
                inword = True           # ... it means that a new word has begun so we need to remember it and...
                word = x                # ... store the first letter of the new word
            else:
                pass
    if inword:                          # if we left the string and there is a non-empty string in word, we need to update the list
        lista.append(word)
    return lista                        # return the list to invoker


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

print(mysplit2("To be or not to be, that is the question"))
print(mysplit2("To be or not to be,that is the question"))
print(mysplit2("   "))
print(mysplit2(" abc "))
print(mysplit2(""))
