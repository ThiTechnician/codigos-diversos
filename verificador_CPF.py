#Thiago M.C. Medeiros
#https://www.linkedin.com/in/thiago-carvalho-2020/
#versão 1.0

print("*******************")
print("VERIFICADOR DE CPF")
print("*******************\n")


#recebe o CPF
cpf = input("Digite seu CPF usando apenas números: ")

#Variáveis auxiliares
lista = list(cpf)
lista_int = []
j = 0

#converte o cpf numa lista de inteiros
def conversor():
    for i in range(0,11):
        j = int(lista[i])
        lista_int.append(j)
    return lista_int

#soma os algarismos do CPF e verifica de a soma resulta em dois algarismos iguais
def validador():
    soma = sum(lista_int)
    soma_str = str(soma)

    if soma_str[0] == soma_str[1]:
        print("CPF válido!")
    else:
        print("CPF inválido!")
conversor()
validador()
