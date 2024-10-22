# Lista de perguntas e respostas
jogar = True
while jogar == True:
    contador=0

pergunta1= input("responda verdadeiro ou falso: Fibonacci significa, dentro do conceito matemático, uma sequência em que cada número seguinte corresponde à soma dos dois anteriores? ")
if pergunta1 == "verdadeiro":
    print("voce acertou")
else:
    print("voce errou")

pergunta2=input("responda verdadeiro ou falso: float permite guardar dados numéricos com parte decimal, o que vem antes ou depois da vírgula? ")
if pergunta2 == "falso":
    print("voce acertou")
else:
    print("voce errou")

pergunta3=input("responda verdadeiro ou falso: O Python foi criado em 1987 pelo programador holandês Guido van Rossum? ")
if pergunta3 == "falso":
    print("você acertou")
else:
    print("voce errou")

jogar = input("deseja jogar novamente? ")
if(jogar == "nao"):
    jogar= False
quantidadedeperguntas=3
if(contador/2<quantidadedeperguntas):
    print()