a=1
b=1
pulo=1
for i in range(10):
    print(a)
    pulo=b-a    #atualiza "pulo" com a distancia entre os numeros
    temp=a      #armazena o valor atual de "a" em uma variavel temporaria
    a=b         #Atualiza "a" com o valor de "b"
    b=temp+b    #atualiza "b" com a soma do antigo "a" e "b"
