# Programa para calcular a soma acumulada de 5 números
valor_total = 0
# Inserira 5 números:
for i in range(5):
    numero = float(input(f"Insira o número {i+2}: "))
    valor_total += numero

#soma total
print(f"A soma acumulada dos números é {valor_total}")
