import os

def acrescenta_ids_ordenados(tam):
  ids_ordenados = []
  for i in range(tam):
    ids_ordenados.append(i)
  return ids_ordenados

def reordena_ids(estrutura_de_dados, tam):
  for i in range(tam):
    estrutura_de_dados[i]["id"] = i
  return estrutura_de_dados

#essa função pode se tornar mais genérica, como: cria arquivo, coloca cabeçalho, coloca
#no arquivo csv a lista de dicionários - ou seja, ser uma função que transforma uma
#lista de dicionários em um csv
def atualiza_registros_em_produto_txt(nome_arquivo, produtos, qtd_registros):
  with open(nome_arquivo, "w") as arquivo:
    arquivo.write('id,nome,descricao,peso,valor,fornecedor\n')
    for i in range(qtd_registros):
      arquivo.write(f'{produtos[i]["id"]},{produtos[i]["nome"]},{produtos[i]["descricao"]},{produtos[i]["peso"]},{produtos[i]["valor"]},{produtos[i]["fornecedor"]}\n')

def cria_registro_em_produto_txt(nome_arquivo, produtos, next_id):
  with open(nome_arquivo, "a") as arquivo:
    arquivo.write(f'{produtos[next_id]["id"]},{produtos[next_id]["nome"]},{produtos[next_id]["descricao"]},{produtos[next_id]["peso"]},{produtos[next_id]["valor"]},{produtos[next_id]["fornecedor"]}\n')

def verifica_cria_arquivo(nome_arquivo, conteudo_inicial):
  if not os.path.exists(nome_arquivo):
    open(nome_arquivo, "a")
    with open(nome_arquivo, "a") as arquivo:
      arquivo.write(conteudo_inicial)
    return False
  else:
    return True
    
def le_linha_csv(linha):
#tentar fazer o split segundo as virgulas, em seguida
#tirar o \n do último campo com replace. Somente vou testar o que acontece
#quando faço um split em uma lista. 
  info_linha = []
  info_linha= linha.split(',')
  last_idx = len(info_linha) - 1
  info_linha[last_idx] = info_linha[last_idx].replace('\n', '')
  return info_linha

def cria_listdicio_com_csv(nome_arquivo):
  
  with open(nome_arquivo, "r") as arquivo:
    csv = arquivo.readlines()

  dic_defs = le_linha_csv(csv[0])
  list_dicio = []
  n_linhas = len(csv)
  
  for i in range(n_linhas - 1):
    list_dicio.append({})
    dados_linha_atual = le_linha_csv(csv[i + 1])
    for j in range(len(dic_defs)):
      list_dicio[i][dic_defs[j]] = dados_linha_atual[j]
  return list_dicio      


#Autenticação
username = input('username: ')
password = input('password: ')

#puxando arquivo para autenticação
verifica_cria_arquivo("./usuario.txt", "root\n123456")

#Criando a autenticação. Primeiro, vamos extrair o login e senha corretos
#do arquivo, em seguida tirar o '\n' do login.
#Depois vamos comparar as variáveis username e password 
#com a do arquivo e não permiti rpassar para a próxima estrutura 
#do programa enquanto não informar o username e password corretos.
#Para realizar a verificação foi posto um while.


#vai ser um read, "r", pois queremos extrair informações desse txt
with open("./usuario.txt", "r") as arquivo:
  login_info = arquivo.readlines()

#aqui, vamos estar tirando, ou deletando o '\n'
login_info[0] = login_info[0].replace('\n', '')

#fazendo a estrutura que não vai permitir continuar enquanto o username
#ou o password forem incorretos- pedindo para reescrever ambos
#se pelo menos um estiver incorreto

while username != login_info[0] or password != login_info[1]:
  print('username ou password invalidos. Tente novamente.')
  username = input('username: ')
  password = input('password: ')

print(f'\nOlá, {username}!\n\n')

#Quando iniciar o programa, já tem de puxar dos dados persistidos em 
#produtos.txt


tem_prod_txt = verifica_cria_arquivo("./produtos.txt", "id,nome,descricao,peso,valor,fornecedor\n")
tem_next_txt = verifica_cria_arquivo("./next_id.txt", "0")
tem_qtdprod_txt = verifica_cria_arquivo("./qtd_prod.txt", "0")


if ((not tem_prod_txt) and tem_next_txt and tem_qtdprod_txt):
  with open("./next_id.txt", "w") as arquivo:
    arquivo.write("0")
  with open("./qtd_prod.txt", "w") as arquivo:
    arquivo.write("0")

with open("./next_id.txt", "r") as arquivo:
    next_id = int(arquivo.read())
with open("./qtd_prod.txt", "r") as arquivo:
    qtd_produtos = int(arquivo.read())
  
 
produtos = []
produtos = cria_listdicio_com_csv("./produtos.txt") 
 
  
resp = 8
while resp != 6:
  print('Digite a operação que deseja realizar:')
  print('(1)Listar Produtos')
  print('(2)Listar segundo a ordem alfabética')
  print('(3)Cadastrar novo produto')
  print('(4)Editar Produto')
  print('(5)Excluir Produto')
  print('(6)Sair do programa\n')
  
  resp = int(input())

  #navegando pelo menu

  match resp:
    case 1:
      for i in range(qtd_produtos):
        print(f'{produtos[i]}\n')
    case 2:
      #colocando uma lista de ids, a qual vamos ordenar
      #(em oposição a alterar a lista de produtos em si) 
      # segundo a ordem alfabetica.
      ids_ordenados = []
      ids_ordenados =  acrescenta_ids_ordenados(qtd_produtos)

      #Aqui, vou fazer a estrutura do Bubble Sort
      k = qtd_produtos
      trocado = True

      
      while trocado:
        trocado = False
        for i in range(k - 1):
          if produtos[ids_ordenados[i]]['nome'] > produtos[ids_ordenados[i + 1]]['nome']:
            temp = ids_ordenados[i]
            ids_ordenados [i] = ids_ordenados[i + 1]
            ids_ordenados[i + 1] = temp
            trocado = True
        k -= 1

      for i in range(qtd_produtos):
          print(produtos[ids_ordenados[i]])
  
      
    case 3:
      produtos.append({})

      #tem o problema, pois não et
      
      print('\n')
      produtos[next_id]['id'] = next_id
      produtos[next_id]['nome'] = input('Digite o nome do produto: ')
      produtos[next_id]['descricao'] = input('Digite a descrição do produto: ')
      produtos[next_id]['peso'] = input('Digite a peso do produto: ')
      produtos[next_id]['valor'] = input('Digite a valor do produto: ')
      produtos[next_id]['fornecedor'] = input('Digite a fornecedor do produto: ')

      with open("./produtos.txt", "a") as arquivo:
          arquivo.write(f'{produtos[next_id]["id"]},{produtos[next_id]["nome"]},{produtos[next_id]["descricao"]},{produtos[next_id]["peso"]},{produtos[next_id]["valor"]},{produtos[next_id]["fornecedor"]}\n')
        
      qtd_produtos += 1
      next_id+=1
     
      with open("./next_id.txt", "w") as arquivo:
        arquivo.write(f"{next_id}")
      with open("./qtd_prod.txt", "w") as arquivo:
        arquivo.write(f"{qtd_produtos}")
        
      print('\n')
    case 4:
      with open("./produtos.txt", "r") as arquivo:
        temp_info_produtos_txt = arquivo.readlines()
     
      querAlterarProdutos='s'
      while querAlterarProdutos == 's':
        edit_idx = int(input('Digite o id do produto que deseja editar: '))
        querEditarCampoDoProduto = 's'
        while querEditarCampoDoProduto == 's':
        
          field = input('Digite o campo que deseja editar:') 
          produtos[edit_idx][field] = input('Digite o novo valor: ')                  
          #Aqui, vamos alterar um item específico da lista. Vamos usar o 
          #readlines para deixar todas as informações de um produto 
          #associadas a um índice na lista. Em seguida, vamos alterar
          #o produto cujo índice é igual a edit_idx. Depois usar write
          #para devolver ao arquivo

          
          atualiza_registros_em_produto_txt("./produtos.txt", produtos, qtd_produtos)
            
          querEditarCampoDoProduto = input('Deseja continuar alterando esse produto? (Resposta: s/n)')
        querAlterarProdutos= input('Deseja continuar alterando produtos? (Resposta: s/n)')

    case 5:
      del_idx = int(input('Digite o id do produto que deseja excluir: ')) 
      del produtos[del_idx]
      
      qtd_produtos -= 1
      with open("./qtd_prod.txt", "w") as arquivo:
        arquivo.write(f'{qtd_produtos}')

      next_id -= 1
      with open("./next_id.txt", "w") as arquivo:
        arquivo.write(f'{next_id}')


      produtos = reordena_ids(produtos, qtd_produtos)

      atualiza_registros_em_produto_txt("./produtos.txt", produtos, qtd_produtos)
