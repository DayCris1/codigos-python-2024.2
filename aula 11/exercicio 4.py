#Em continuação ao exercício 1, enquanto o aventureiro segue o caminho na floresta, um bandido o ataca

inventario = ["espada", "escudo", "poção"]
print("Inventário inicial:", inventario)

print("\nEnquanto você segue seu caminho pela floresta, um bandido armado surge e exige que você entregue sua poção!")

# Verificando se o jogador tem a espada para lutar
opção = input("O que você fará? (1 - Usar a espada, 2 - Entregar a poção): ")

if opção == "1":
    if "espada" in inventario:
        print("Você saca sua espada e enfrenta o bandido!")
        print("Após uma luta feroz, você derrota o bandido e continua sua jornada.")
    else:
        print("Você não tem uma espada! Sem defesa, o bandido te derrota facilmente.")
        print("Fim de jogo!")
elif opção == "2":
    if "poção" in inventario:
        inventario.remove("poção")
        print("Você entrega a poção ao bandido, e ele vai embora satisfeito.")
        print("Você perdeu a poção, mas está vivo.")
    else:
        print("Você não tem uma poção para entregar!")
        print("Furioso, o bandido te ataca e você não consegue escapar.")
        print("Fim de jogo!")
else:
    print("Decisão inválida. O bandido aproveita sua hesitação e te derrota.")
    print("Fim de jogo!")