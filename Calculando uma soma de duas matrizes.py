def ler_matriz(col, lin):
    matriz = []
    for i in range(lin):
        linhamatriz = []
        for j in range(col):
            valor = int(input("Digite os valores da posição da matriz [{}][{}]: ".format(i,j)))
            linhamatriz.append(valor)
    matriz.append(linhamatriz)
    return matriz

def SomaMatriz(matriz1, matriz2):
    matriz = []
    for i in range(len(matriz1)):
        linhasoma  = []
        for j in range(len(matriz2[0])):
            valor = matriz1[i][j] + matriz2[i][j]
            linhasoma.append(valor)
    matriz.append(linhasoma)
    return matriz

def SubtracaoMatriz(matriz1, matriz2):
    matriz = []
    for i in range(len(matriz1)):
        linhasubtracao = []
        for j in range(len(matriz2[0])):
            valor = matriz1[i][j] - matriz2[i][j]
            linhasubtracao.append(valor)
    matriz.append(linhasubtracao)
    return matriz

def fazer_operacao (matriz1, matriz2, operacao):
    if operacao == 1:
        return SomaMatriz(matriz1, matriz2)
    elif operacao == 2:
        return SubtracaoMatriz(matriz1, matriz2)
 
def perguntacalculo():
    print("Escolha uma opção:")
    print("1 - Somar Matriz")
    print("2 - Subtrair Matriz")
    print("0 - Finalizar")
    return int(input("R: "))
  

def pergunta():
    print("Escolha uma opção:")
    print("1 - Adicionar Matriz")
    print("2 - Calcular a Soma ou Subtração da Matriz")
    print("0 - Finalizar")
    return int(input("R: "))
 
opcao = pergunta()
while opcao != 0:
    if opcao == 1:
        col = int(input("Digite a quantidade de colunas da matriz: "))
        lin = int(input("Digite a quantidade de linha da matriz: "))
        matriz1 = ler_matriz(col, lin)
        matriz2 = ler_matriz(col, lin)
    elif opcao == 2:
        operacao = perguntacalculo()
        if operacao == 1:
            soma = fazer_operacao(matriz1, matriz2, operacao)
            print("A primeira matriz {} \nA segunda matriz {}" .format(matriz1,matriz2))
            print("Resultado da soma das matrizes resultantes é {}" .format(soma))
        elif operacao == 2:
            subtracao = fazer_operacao(matriz1, matriz2, operacao)
            print("A primeira matriz {} \nA segunda matriz {}" .format(matriz1,matriz2))
            print("Resultado da subtração das matrizes resultantes é {}" .format(subtracao))
        else:
            opcao = pergunta() 
    opcao = pergunta() 
      
