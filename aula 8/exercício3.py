#FAÇA UM PROGRAMA QUE PEÇA 5 NUMEROS AO USUARIO E SOMA NO FINAL
soma=0
for i in range(5):
    numero= float(input("Insira um número: "))
    soma += numero
print(f"a soma total é: {soma}")