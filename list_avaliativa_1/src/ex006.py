#Autenticação
username = input('Digite seu nome de usuario: ')
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
  print('(5)Excluir Produto\n')
  
  resp = int(input())

  #navegando pelo menu

  match resp:
    case 1:
      prod_len = len(produtos)
      for i in range(prod_len):
        print(f'{produtos[i]}\n')
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
          
      
      
    
 
