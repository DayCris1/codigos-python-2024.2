import random

#Gera um numero inteiro aleatorio entre 1 e 100:
numero_aleatorio = random.randint(1, 100)
print(f"numero inteiro aleatorio entre 1 e 100: {numero_aleatorio}")

print("entre com dois numero, irei retornar com um numero aleatorio entre eles")
numero_usuario_menor=int(input("entre com o menor deles" ))
numero_usuario_maior=int(input("entre com o maior deles" ))
numero_aleatorio2=random.randint(numero_usuario_menor, numero_usuario_maior)

print(f"numero inteiro aleatório entre: {numero_usuario_menor} e {numero_usuario_maior}: {numero_aleatorio2}")