#FAÇA UM PROGRAMA QUE GERE 3 NÚMEROS ALEATÓRIOS (FLOAT) ENTRE 1 E 15 E VOCE TEM 1 TENTATIVA PARA DESCOBRIR QUAL É O MAIOR

import random

# Gerar três números aleatórios entre 1 e 15
num1 = random.uniform(1, 15)
num2 = random.uniform(1, 15)
num3 = random.uniform(1, 15)

# Exibir os números gerados
print(f"Números gerados:{num1:.2f},{num2:.2f},{num3:.2f}")

# Solicitar ao usuário que adivinhe qual é o maior número
tentativa = float(input("Qual é o maior número? "))

# Determinar o maior número
maior_numero = max(num1, num2, num3)

# Verificar se a tentativa do usuário está correta
if tentativa == maior_numero:
    print("arrasou!")
else:
    print(f" Vc errou, O CORRETO: {maior_numero:.2f}.")

