#Função: Calcula A DIVISÃO de um numero

def divisao(numero):
    return numero / 2

numero = float(input("digite um numero: "))
resultado = divisao(numero) #recebe o retorno da função
print(f"O quadrado de {numero} é {resultado}")