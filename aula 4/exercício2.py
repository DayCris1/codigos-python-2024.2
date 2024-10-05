# quantas rodas tem um veículo
rodas=int(input("quantas rodas tem o veículo?"))
if(rodas==4):
    print("o veículo é uma van ou um carro")
elif(rodas==2):
    print("o veiculo é uma moto")
elif(rodas==6):
    print("o veículo é um onibus")
elif(rodas>=8 and rodas<=20):
    print("o veículo é um caminhão")


else:
    print("não foi encontrado um veículo correspondente ao número de rodas")

