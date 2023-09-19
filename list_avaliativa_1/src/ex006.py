produtos = []

#Autenticação
username = input('Digite seu nome de usuario: ')
print(f'\nOlá, {username}!\n\n')

#Seleção da função

resp = 8
while resp != 6:
  print('Digite a operação que deseja realizar:\n')
  print('(1)Listar Produtos\n')
  print('(2)Listar segundo a ordem alfabética\n')
  print('(3)Cadastrar novo produto\n')
  print('(4)Editar Produto\n')
  print('(5)Excluir Produto')
  
  resp = int(input())

  #navegando pelo menu

  match resp:
    case 3:
      produtos.append({})
      
      last_idx = len(produtos) - 1
      print(last_idx)
      
      produtos[last_idx]['id'] = last_idx
      produtos[last_idx]['nome'] = input('Digite o nome do produto: ')
      produtos[last_idx]['descricao'] = input('Digite a descrição do produto: ')
      produtos[last_idx]['peso'] = input('Digite a peso do produto: ')
      produtos[last_idx]['valor'] = input('Digite a valor do produto: ')
      produtos[last_idx]['fornecedor'] = input('Digite a fornecedor do produto: ')
      print(produtos[last_idx])
    
 
