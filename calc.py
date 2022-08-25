#Calculadora simples entre 2 números

número1 = eval(input('Digite o primeiro número: '))
número2 = eval(input('Digite o segundo número: '))
operação = str(input('Qual das 4 operações básicas vc deseja executar ? '))
soma = número1 + número2
divisão = número1 // número2 or número1 / número2
subtração = número1 - número2
multiplicação = número1 * número2

if operação == '+' or operação == 'soma' or operação == 'somar':
    print(f'A soma entre {número1} e {número2} é igual a {soma}')
elif operação == '-' or operação == 'diminuir' or operação == 'subtração':
    print(f'A subtração entre {número1} e {número2} deu {subtração}')
elif operação == '/' or operação == 'dividir' or operação == 'divisão':
    print(f'A divisão entre {número1} e {número2} deu {divisão:.1f}')
elif operação == '*' or operação == 'multiplicação' or operação == 'x' or operação == 'multiplicar':
    print(f'A multiplicação entre {número1} e {número2} deu {multiplicação}')
print('A operação chegou ao fim...')
