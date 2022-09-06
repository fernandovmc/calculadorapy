operation = input('''
Escolha a operação desejada para fazer os calculos:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if operation == '+':
    print(f'{num1} + {num2} = {num1+num2}')
if operation == '-':
    print(f'{num1} - {num2} = {num1-num2}')
if operation == '*':
    print(f'{num1} * {num2} = {num1*num2}')
if operation == '/':
    print(f'{num1} / {num2} = {num1/num2}')
else:
    print(f'''
Operação escolhida inválida. 
Tente novamente e escolha somente as operações mostradas.
''')