#Faça um programa que tenha uma função chamada converter. Essa Função deve receber uma temperatura em celcius e retornar em fahreinheit.
def converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp =float(input("insira a temperatura: "))
resultado = converter(temp)
print(f"o resultado de fahrenheit é {resultado}°F")

