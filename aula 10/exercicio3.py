#criando uma lista simples com 3 pokémons
pokemons = ["Pickachu", "charmander", "Bulbasaur"]

#Exibindo a lista
print("Lista de Pokemons:", pokemons)

#Acessando o primeiro o Pokemon à lista
print("Primeiro Pokemon:", pokemons[0])

#Adcionando um novo Pokemon a lista
pokemons.append("Squirtle")
print("Lista de Pokemons apos o Squirtle:", pokemons)

#Removendo o Pokemon "Charmander" da lista
pokemons.remove("charmander")
print("Lista de Pokemons apos remover Charmander:", pokemons)

#Exibindo o tamanho da lista
print("numero de Pokemons na lista :", len(pokemons))
