#Inicie a lista com o pikachu com 4 poderes: lista[choque dotrovão, calda de ferro, ataque rapido, esquiva]

#criando a lista com os poderes
poderes = ["choque do trovão", "calda de ferro", "ataque rapido", "esquiva"]

#Insira aqui o novo poder
novopoder = input("digite aqui um novo poder: ")
poderes.append(novopoder)
print("lista de poderes após adcionar o novo poder:", poderes)

#remova o choque do trovão da lista
poderes.remove("choque do trovão")
print("lista de poderes após remover choque do trovão", poderes)

#exibindo o tamanho da lista
print("numero de poderes na lista:", len(poderes))

