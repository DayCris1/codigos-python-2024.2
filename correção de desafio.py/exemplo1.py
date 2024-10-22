# Inicializa os dois primeiros números da sequência
a, b = 0, 1

# Imprime os 10 primeiros números da sequência de Fibonacci
for i in range(10):
    print(a)
    a, b = b, a + b
