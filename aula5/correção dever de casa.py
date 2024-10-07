numero=int(input("digite um numero"))

if numero % 3==0:
        print(f"o numero {numero} é divisivel por 3")
        if numero %5==0:
                print(f"o numero {numero} é divisivel por 5")
elif numero % 5==0:
        print(f"o numero {numero} é divisivel por 5")
else:
        print(f"o numero {numero} não é divisivel nem por 3 e nem por 5")
        
