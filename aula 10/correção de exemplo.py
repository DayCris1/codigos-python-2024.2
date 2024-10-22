import random

numero1 = random.randint(20, 50)
numero2 = random.randint(20, 50)
numero3 = random.randint(20, 50)
numero4 = random.randint(20, 50)
numero5 = random.randint(20, 50)

print(f"numeros gerados: {numero1} {numero2} {numero3} {numero4} {numero5}")


for i in range(5):
    if numero1 < numero2:  
        numero1, numero2 = numero2, numero1
    if numero1 < numero3:
        numero1, numero3 = numero3, numero1
    if numero1 < numero4:
        numero1, numero4 = numero4, numero1
    if numero2 < numero3:
        numero2, numero3 = numero3, numero2
    if numero2 < numero4:
        numero2, numero4 = numero4, numero2
    if numero3 < numero4:
        numero3, numero4 = numero4, numero3


print(f"Números ordenados decrescentemente: {numero1}, {numero2}, {numero3}, {numero4}")