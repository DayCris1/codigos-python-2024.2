#peça 2 numeros e faça uma operação com base no seguinte menu, 1 - soma dos dois numeros, 2-subtrai os dois numeros, 3-multiplica os dois numeros e 4-dividir os dois numeros:

# Solicita ao usuário que insira dois números
x1 = float(input("Digite o primeiro número: "))
x2 = float(input("Digite o segundo número: "))

# Exibe o menu de operações
print("Escolha a opção desejada:")
print("1 - Soma")
print("2 - Subtrai")
print("3 - Multiplica")
print("4 - Divide")

# digite a opção:
opção = int(input("Digite o número: "))

# Realiza a opção escolhida e exibe o resultado
if opção == 1:
    resultado = x1 + x2
    print(f"\nResultado: {x1} + {x2} = {resultado}")
elif opção == 2:
    resultado = x1 - x2
    print(f"\nResultado: {x1} - {x2} = {resultado}")
elif opção == 3:
    resultado = x1 * x2
    print(f"\nResultado: {x1} * {x2} = {resultado}")
elif opção == 4:
    if x2 != 0:
        resultado = x1 / x2
        print(f"\nResultado: {x1} / {x2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
