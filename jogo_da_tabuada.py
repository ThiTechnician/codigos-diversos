#versão 1.0
#criador: Thiago M.C.Medeiros
#https://www.linkedin.com/in/thiago-carvalho-2020/
from random import randint

print("****************")
print("APRENDA TABUADA")
print("****************")
pontos = 5

while True:
    a = randint(0,9)
    b = randint(0,9)
    print("Pontos: ",pontos)
    print(a ," x ",b," = " ,end= " ")
    resultado = a * b
    resposta = input("")

    if int(resposta) == resultado:
        print("COCRRETO!")
        pontos = pontos + 10
    else:
        print("ERROU!")
        pontos = pontos - 10
    if pontos >= 100:
        print("VOCÊ VENCEU O JOGO!")
        break
    elif pontos < 0:
        print("VOCÊ PERDEU O JOGO!")
        break
