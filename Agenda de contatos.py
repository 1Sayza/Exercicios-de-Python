# Faça um programa que implemente uma agenda de contatos simples com a menor repetição de código possível e uso de funções. Os dados dos contatos da agenda devem ser armazenadas em uma variável global do tipo dicionário. O programa deve ficar em loop até que o usuário decida encerrá-lo.

# Dados de entrada:

# Nome do contato (Deve permitir nomes repetidos)
# Número de telefone (Pode ter vários por contato)
# Processamento:

# Adicionar contato: Cria um novo contato na agenda
# Listar contato: Lista todos os contatos da agenda (Deve percorrer a agenda inteira e exibir os contatos)
# Buscar contato: Localiza um contato na agenda com base em uma String de busca informada pelo usuário
# Remover contato: Deleta um contato na agenda

def pergunta():
  print("Escolha uma opção: ")
  print("1 - Adicionar contato")
  print("2 - Listar contato da agenda")
  print("3 - Buscar contato")
  print("4 - Remover contato")
  print("0 - Sair")
  return int(input("R: "))

def pergunta2():
  print("Escolha uma opção: ")
  print("1 - Adicionar telefone para o contato")
  print("0 - Sair")
  return int(input("R: "))

def Mostrarcontato(nome, lista):
  print("\tNome: {}".format(nome))
  cont = 1
  for l in lista:
      print("\t\t {} Contato {}".format(cont, l))
      cont += 1
    
def Mostrarcontatos(dic):
    print("______________________________")

    for key in dic:
        Mostrarcontato(key,dic[key])

    print("______________________________")

def AddContato(dic):
  agenda = input("Digite o nome do contato: ")
  dic[agenda] = []
  cont = 1
  

def Buscarcontato(dic):
  contato = input("Digite o nome do contato: ")
  if contato in dic:
    Mostrarcontato(contato, dic[contato])
  else:
    print("Contato não existe!")
 
def Removercontato(dic):
  contato = input("Digite o nome do contato: ")
  if contato in dic:
    dic.pop(contato)
    print("Removido o contato")
  else:
    print("Contato não existe!")

dicionario = {}
opcao = pergunta()
while opcao != 0:
  if opcao == 1:
    AddContato(dicionario)
  elif opcao == 2:
    Mostrarcontatos(dicionario)
  elif opcao == 3:
    Buscarcontato(dicionario)
  elif opcao == 4:
    Removercontato(dicionario)
    
  opcao = pergunta()