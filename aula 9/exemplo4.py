import random

#Simula o lançamento da moeda
resultado="Cara" if random.randint(0, 1)== 0 else "Coroa"
print(f"o resultado do lançamento da moeda é: {resultado}")
