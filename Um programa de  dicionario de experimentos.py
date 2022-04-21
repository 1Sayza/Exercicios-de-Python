# A tabela abaixo ilustra o conjunto de dados obtidos por um pesquisador em seus experimentos científicos. O pesquisador deseja inserir (digitar) os dados # de cada experimento em um programa de computador e obter como resultado os valores de média, variância e desvio padrão das variáveis de cada experimento.

# Experimento	var1	var2	var3	...
# Exp1	8	3	10	...
# Exp2	10	2	3	...
# Exp3	7	8	2	...
# ...	...	...	...	...

def pergunta():
    print("Escolha uma opção:")
    print("1 - Adc Exp")
    print("2 - Mostrar Exp")
    print("3 - Calcular Exp")
    print("0 - Sair")
    return int(input("R: "))

def pergunta2():
    print("Escolha uma opção:")
    print("1 - Adc Amostra")
    print("0 - Sair")
    return int(input("R: "))

def pergunta3():
    print("Escolha uma opção:")
    print("1 - Especifico")
    print("2 - Todos")
    print("0 - Sair")
    return int(input("R: "))
    
def AddExp(dic):
    key = input("Digite o nome do experimento: ")
    dic[key] = []
    cont = 1
    while True:
        opc = pergunta2()
        if opc == 1:
            valor = int(input("Digite o valor da amostra{}: ".format(cont)))
            dic[key].append(valor)
            cont += 1
        elif opc == 0:
            print("Saindo...")
            break
        else:
            print("Opção invalida!")

def MostrarExp(dic):
    print("______________________________")

    for key in dic:
        print("\tExp: {}".format(key))
        cont = 1
        for l in dic[key]:
            print("\t\tAmotra{} {}".format(cont, l))
            cont += 1

    print("______________________________")

def Media(lista):
   return sum(lista) / len(lista)

def Desvio(lista):
    listaDesvio = []
    media = Media(lista)
    for valor in lista:
        if media < valor:
            listaDesvio.append(valor - media)
        elif media > valor:
            listaDesvio.append(media - valor)

    return listaDesvio

def Variancia(media,listaDesvio):
    soma = 0
    for desvio in listaDesvio:
        soma += desvio**2
    variancia = soma / media

    return variancia

def DesvioPadrao(variancia):
    dp = variancia**1/2
    return dp

def CalcularExp(dic):
    while True:
        opc = pergunta3()
        if opc == 1:
            MostrarExp(dic)
            key = input("Digite o nome do experimento: ")
            if key in dic:
                media = Media(dic[key])
                print("A media do experimento {} é {}".format(key, media))
                variancia = Variancia(media,Desvio(dic[key]))
                print("A variância do experimento {} é {}" .format(key, variancia))
                print(" O desvio padrão do experimento {} é {}" .format(key, DesvioPadrao(variancia)))
            else:
                print("Chave invalida")
        elif opc == 2:
            for key in dic:
                 print("A média do experimento {} é {}".format(key, Media(dic[key])))
        elif opc == 0:
            print("Saindo...")
            break
        else:
            print("Opção invalida!")

dicionario = {}
opcao = pergunta()
while opcao != 0:
    if opcao == 1:
        AddExp(dicionario)
    elif opcao == 2:
        MostrarExp(dicionario)
    elif opcao == 3:
        CalcularExp(dicionario)
    opcao = pergunta()
print(dicionario)

print("Finalizado!!!!")

