print("bem vindo ao lava rapido")
escolhalavagem=int(input("escolha qual o tipo de lavagem gostaria para seu veículo"))
opção1 = "lavagemcompleta"
opção2 = "lavagembasica"
if(escolhalavagem==1):
      print (f"voce escolheu {opção1}")
      valor_total = 50.00

elif(escolhalavagem==2):
      print(f"voce escolheu {opção2}")
      valor_total= 35
else:
      print("inválida")
adicionar_pretinho=(input("deseja adicionar pretinho por mais R$5.00?"))
if(adicionar_pretinho  == "sim"):
    valor_total+=5.00
    print (f"voce escolheu {valor_total} com pretinho")
else:
    print(f"o serviço de {escolhalavagem}será no total de R$ {valor_total}")

   







