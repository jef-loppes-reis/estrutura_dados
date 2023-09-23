#Autenticação
username = input('username: ')
password = input('password: ')

#Criando a autenticação. Primeiro, vamos extrair o login e senha corretos
#do arquivo, em seguida tirar o '\n' do login.
#Depois vamos comparar as variáveis username e password 
#com a do arquivo e não permiti rpassar para a próxima estrutura 
#do programa enquanto não informar o username e password corretos.
#Para realizar a verificação foi posto um while.


#vai ser um read, "r", pois queremos extrair informações desse txt
with open("usuario.txt", "r") as arquivo:
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

#Seleção da função
produtos = []

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
      prod_len = len(produtos)
      for i in range(prod_len):
        print(f'{produtos[i]}\n')
    case 2:
      #colocando uma lista de ids, a qual vamos ordenar
      #(em oposição a alterar a lista de produtos em si) 
      # segundo a ordem alfabetica.
      ids_ordenados = []
      #criando a variável num_prod para armazenar a quantidade
      #de produtos, a qual vai ser utilizada dentro de um for
      #para receber todos os ids.

      num_prod = len(produtos)
      
      #fazendo um for para atribuir todos os ids -  

      for i in range (num_prod):
        ids_ordenados.append(produtos[i]['id'])

      #Aqui, vou fazer a estrutura do Bubble Sort
      k = num_prod
      trocado = True
      #Por que num_prod - 1?
      while trocado:
        trocado = False
        for i in range(k - 1):
          if produtos[i]['nome'] > produtos[i + 1]['nome']:
            temp = ids_ordenados[i]
            ids_ordenados [i] = ids_ordenados[i + 1]
            ids_ordenados[i + 1] = temp
            trocado = True
          k -= 1

      for i in range(num_prod):
          print(produtos[ids_ordenados[i]])
  
      
    case 3:
      produtos.append({})
      
      last_idx = len(produtos) - 1

      print('\n')
      produtos[last_idx]['id'] = last_idx
      produtos[last_idx]['nome'] = input('Digite o nome do produto: ')
      produtos[last_idx]['descricao'] = input('Digite a descrição do produto: ')
      produtos[last_idx]['peso'] = input('Digite a peso do produto: ')
      produtos[last_idx]['valor'] = input('Digite a valor do produto: ')
      produtos[last_idx]['fornecedor'] = input('Digite a fornecedor do produto: ')

    case 4:
      querAlterarProdutos='s'
      
      while querAlterarProdutos == 's':
        edit_idx = int(input('Digite o id do produto que deseja editar: '))
        querEditarCampoDoProduto = 's'
        while querEditarCampoDoProduto == 's':
        
          field = input('Digite o campo que deseja editar:') 
          produtos[edit_idx][field] = input('Digite o novo valor: ')
          querEditarCampoDoProduto = input('Deseja continuar alterando esse produto? (Resposta: s/n)')
        querAlterarProdutos= input('Deseja continuar alterando produtos? (Resposta: s/n)')

    case 5:
      del_idx = int(input('Digite o id do produto que deseja excluir: '))
      del produtos[del_idx]
    
          
      
      
    
 
