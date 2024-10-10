#Faça um programa que peça 1 numero ao cliente e faça sua tabuada (até o 10)

numero = int(input("Digite um número para ver sua tabuada: "))
x =1

print(f"a tabuada do {numero} é")
while x<=10:
    multiplica = numero * x
    print(f"{numero} x {x} = {multiplica}")
    x+=1






