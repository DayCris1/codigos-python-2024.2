EscolhaLanche = int(input("-------------------Bem Vindo ao Maquimeleca, qual opção você gostaria?---------------------\n Digite 1 para Hamburguer - R$10,00 \n Digite 2 para Batata Frita  - R$10,00 \n Digite 3 para refrigerente - R$10,00 \n Digite 4 para combo (os 4 itens) - R$22,00 \n"))
item1 = "Hamburguer"
item2 = "Batata Frita"
item3 = "Refrigerante"
item4 = "Combo"

if(EscolhaLanche == 1):
    print(f"Você escolheu {item1}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 2 para Batata Frita e Digite 3 para refrigerante"))
    if (adicional == 2):
        print(f"Você escolheu {item1} e {item2}")
        oferecercombo = input("Gostaria de adicionar o mais um item por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item2},  totalizando R$20,00")
    elif (adicional == 3):
        print(f"Você escolheu {item1} e {item3}")
        oferecercombo = input("Gostaria de adicionar o refrigerante por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {item1},  totalizando R$10,00") 

if(EscolhaLanche == 2):
    print(f"Você escolheu {item2}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 1 para Hamburguer e Digite 3 para refrigerente"))
    if(adicional == 1):
        print(f"Você escolheu {item2} e {item1}")
    oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?").lower()
    if(oferecercombo == "sim"):
        print(f"Seu pedido é {item2} + {item1} + {item3}, totalizando R$22,00")
else:
    print(f"Seu pedido é {item2} + {item1},  totalizando R$20,00")
if(adicional == 3):
    print(f"Você escolheu {item1} e {item3}")
oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?").lower()
if(oferecercombo == "sim"):
    print(f"Seu pedido é {item2} + {item1} + {item3}, totalizando R$22,00")
else:
    print(f"Seu pedido é {item1} + {item3},  totalizando R$20,00")
    print(f"Seu pedido é {item2},  totalizando R$10,00") 

if(EscolhaLanche == 3):
    print(f"Você escolheu {item3}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 1 para Hamburguer e Digite 2 para batata frita"))
elif(adicional == 1):
    print(f"Você escolheu {item3} e {item1}")
    oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?").lower()
    if(oferecercombo == "sim"):
        print(f"Seu pedido é {item3} + {item1} + {item2}, totalizando R$22,00")
else:
    print(f"Seu pedido é {item3} + {item1},  totalizando R$20,00")
if(adicional == 2):
    print(f"Você escolheu {item1} e {item3}")
oferecercombo = input("Gostaria de adicionar batata frita por mais R$2,00?").lower()
if(oferecercombo == "sim"):
    print(f"Seu pedido é {item2} + {item1} + {item3}, totalizando R$22,00")
else:
    print(f"Seu pedido é {item1} + {item3},  totalizando R$20,00")
    print(f"Seu pedido é {item3},  totalizando R$10,00") 

if(EscolhaLanche == 4):
    print(f"Você escolheu {item4}")
    print(f"Seu pedido é {item2} + {item1} + {item3}, totalizando R$22,00")




    
    
