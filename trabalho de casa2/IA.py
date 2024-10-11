def main():
    print("Bem-vindo ao programa de reciclagem!")
    
    # Dicionário para armazenar a contagem de materiais reciclados
    contagem = {
        "papel": 0,
        "plástico": 0,
        "vidro": 0,
        "metal": 0,
        "orgânico": 0,
        "não reciclável": 0
    }
    
    # Dicionário para armazenar as cores das lixeiras
    lixeiras = {
        "papel": "azul",
        "plástico": "vermelha",
        "vidro": "verde",
        "metal": "amarela",
        "orgânico": "marrom",
        "não reciclável": "cinza"
    }
    
    while True:
        material = input("Informe o tipo de material que deseja reciclar (papel, plástico, vidro, metal, orgânico, não reciclável): ").lower()
        
        if material in lixeiras:
            print(f"Descarte o {material} na lixeira {lixeiras[material]}.")
            contagem[material] += 1
        else:
            print("Erro, tente novamente.")
        
        continuar = input("Deseja continuar reciclando? (s/n): ").lower()
        if continuar != 's':
            break
    
    print("\nResumo da reciclagem:")
    for material, quantidade in contagem.items():
        print(f"{material.capitalize()}: {quantidade}")
    
    print("Obrigado por contribuir com a reciclagem!")

if __name__ == "__main__":
    main()
