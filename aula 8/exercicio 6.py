#FAÇA UM PROGRAMA QUE DIGA QUAL DOS 20 PRIMEIROS SÃO MULTIPLOS DE 5 SÃO PARES


for i in range(5, 101, 5):
    if (i % 2 == 0):
        print(i)

#SOME OS IMPARES E MOSTRE ESSA SOMA NO FINAL 
        soma=0     
for i in range(5, 101, 5):
    if (i % 2 !=0):
        print(i)
        soma+=i

print(f"A soma dos números impares deu: {soma}")