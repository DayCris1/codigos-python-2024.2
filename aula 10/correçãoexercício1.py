#FAÇA UM PROGRAMA QUE GERE 3 NÚMEROS ALEATÓRIOS (FLOAT) ENTRE 1 E 15 E VOCE TEM 1 TENTATIVA PARA DESCOBRIR QUAL É O MAIOR
#outra forma de fazer

import random

numero1 = random.uniform(1, 15)
numero2 = random.uniform(1, 15)
numero3 = random.uniform(1, 15)

escolha = int(input("o sistema tem 3 numeros, qual dos 3 você acha que é maior?"))

if escolha == 1 and numero1>numero2 and numero1>numero3:
    print("vc acertou o primeiro numero era o maior")
elif escolha == 2 and numero2>numero1 and numero2>numero3:
    print("vc acertou, o segundo numero era o maior")
elif escolha == 3 and numero3>numero2 and numero1>numero2:
    print("vc acertou, o terceiro era o maior numero")

else:
    print("vc errou")
print("os valores eram:")
print(numero1)
print(numero2)
print(numero3)
                                
