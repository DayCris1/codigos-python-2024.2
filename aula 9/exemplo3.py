#JOGO DO PALPITE
import random




#Gera um numero inteiro aleatorio entre 1 e 100:

numero_aleatorio = random.randint(1, 200)
for i in range (10):
        palpite = float(input("Insira um número: "))
if palpite<=numero_aleatorio:
        print(f"palpite é menor que o numero aleatorio")
else:
        print(f"palpite é maior que o numero aleatorio")
if palpite == numero_aleatorio:
        print("arrasou, vc acertou o palpite")


    


print(f"numero inteiro aleatório: {numero_aleatorio}")


