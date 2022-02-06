while True:
    num = int(input('Digite um número: '))
    num2 = num      # só para usar no for
    if num >= 0:
        break
fact = 1
print(f'{num}! = ', end='')
while num > 0:
    fact *= num
    print(num, end=' x ' if num > 1 else ' = ')     # usando um if dentro do 'end=' para exibir x ou =
    num -= 1
print(f'{fact}')

fact4 = 1
print(f'{num2}! = ', end='')
for i in range(num2, 0, -1):
    fact4 *= i
    print(i, end=' x ' if i > 1 else ' = ')     # usando um if dentro do 'end=' para exibir x ou =
print(f'{fact4}')
