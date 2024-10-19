import random

#gerando 4 numeros aleatorios e armazenando em uma lista
numero=[random.randint(20,50) for i in range(4)]

#exibindo os numeros gerados

print(f"numeros gerados {numero}")

#ordenando os numeros com a função sort

numero.sort()
numero.reverse()

print(f"numeros ordenados: {numero}")
