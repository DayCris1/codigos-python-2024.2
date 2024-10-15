#Faça um programa usando for que peça 4 numeros e some apenas os numeros pares

soma=0
for i in range(4):
    numero=float(input("insira um numero: "))
    if numero % 2 !=0:
        soma += numero

print(f"A soma dos números impares deu: {soma}")
