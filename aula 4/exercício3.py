#Calcule o IMC e classifique
peso=float(input("coloque o peso:"))
altura=float(input("coloque a altura:"))
IMC=(peso/(altura*altura))
print(f"o IMC é: {IMC}")

if (IMC<18.5):
    print("MAGREZA")
elif(IMC>=18.5 and IMC<=24.9):
    print("normal")
elif(IMC>=25 and IMC<=29.9):
    print("sobrepeso")
elif(IMC>=30 and IMC<=39.9):
    print("obesidade")
elif(IMC>=40):
    print("Obesidade grave")