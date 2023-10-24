from os.path import dirname, exists
from os import mkdir
from getpass import getpass


def acrescenta_ids_ordenados(tam):
    ids_ordenados = []
    for i in range(tam):
        ids_ordenados.append(i)
    return ids_ordenados


def reordena_ids(estrutura_de_dados, tam):
    for i in range(tam):
        estrutura_de_dados[i]["id"] = i
    return estrutura_de_dados

# essa função pode se tornar mais genérica, como: cria arquivo, coloca cabeçalho, coloca
# no arquivo csv a lista de dicionários - ou seja, ser uma função que transforma uma
# lista de dicionários em um csv


def atualiza_registros_em_produto_txt(nome_arquivo, produtos, qtd_registros):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write('id,nome,descricao,peso,valor,fornecedor\n')
        for i in range(qtd_registros):
            arquivo.write(f'{produtos[i]["id"]}, {produtos[i]["nome"]}, {produtos[i]["descricao"]}, {
                          produtos[i]["peso"]}, {produtos[i]["valor"]}, {produtos[i]["fornecedor"]}\n')


def cria_registro_em_produto_txt(nome_arquivo, produtos, next_id):
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f'{produtos[next_id]["id"]}, {produtos[next_id]["nome"]}, {produtos[next_id]["descricao"]}, {
                      produtos[next_id]["peso"]}, {produtos[next_id]["valor"]}, {produtos[next_id]["fornecedor"]}\n')


def verifica_cria_arquivo(path, nome_arquivo, conteudo_inicial):
    if not exists(f"{path}/../data"):
        mkdir(f"{path}/../data")
    if not exists(nome_arquivo):
        open(nome_arquivo, "a")
        with open(nome_arquivo, "a") as arquivo:
            arquivo.write(conteudo_inicial)
        return False
    else:

        return True


def le_linha_csv(linha):
    # tentar fazer o split segundo as virgulas, em seguida
    # tirar o \n do último campo com replace. Somente vou testar o que acontece
    # quando faço um split em uma lista.
    info_linha = []
    info_linha = linha.split(',')
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


def bubble_sort_listdic(listdic, campo, crescente):
    size = len(listdic)
    ids_ordenados = acrescenta_ids_ordenados(size)

    trocado = True
    if crescente:
        while trocado:
            trocado = False
            for i in range(size - 1):
                if produtos[ids_ordenados[i]][campo] > produtos[ids_ordenados[i + 1]][campo]:
                    temp = ids_ordenados[i]
                    ids_ordenados[i] = ids_ordenados[i + 1]
                    ids_ordenados[i + 1] = temp
                    trocado = True
    else:
        while trocado:
            trocado = False
            for i in range(size - 1):
                if produtos[ids_ordenados[i]][campo] < produtos[ids_ordenados[i + 1]][campo]:
                    temp = ids_ordenados[i]
                    ids_ordenados[i] = ids_ordenados[i + 1]
                    ids_ordenados[i + 1] = temp
                    trocado = True

    return ids_ordenados


def selection_sort_listdic(listdic, campo, crescente):
    size = len(listdic)
    idx_maior = 0
    idx_menor = size - 1
    aux = 0
    ids_ordenados = acrescenta_ids_ordenados(size)

    if crescente:
        for i in range(size - 1, -1, -1):
            idx_menor = i

            for j in range(i - 1, -1, -1):
                # O problema, penso, é que estava comparando
                # um valor na lista que já havia sido comparado
                if listdic[ids_ordenados[j]][campo] < listdic[ids_ordenados[idx_menor]][campo]:
                    idx_menor = j  # preciso mudar o nome de idx_menor. Ele indica
                    # a posição em ids_ordenados em que tem o índice que, quando colocado em listdic
                    # traz o dic que tem o maior valor dentro de um campo
            aux = ids_ordenados[i]
            ids_ordenados[i] = ids_ordenados[idx_menor]
            ids_ordenados[idx_menor] = aux

    else:
        for i in range(size):
            idx_maior = i

            for j in range(i + 1, size):
                # O problema, penso, é que estava comparando
                # um valor na lista que já havia sido comparado
                if listdic[ids_ordenados[j]][campo] > listdic[ids_ordenados[idx_maior]][campo]:
                    idx_maior = j  # preciso mudar o nome de idx_maior. Ele indica
                    # a posição em ids_ordenados em que tem o índice que, quando colocado em listdic
                    # traz o dic que tem o maior valor dentro de um campo
            aux = ids_ordenados[i]
            ids_ordenados[i] = ids_ordenados[idx_maior]
            ids_ordenados[idx_maior] = aux

    return ids_ordenados


def insertion_sort_listdic(listdic, campo, crescente):
    size = len(listdic)
    aux = 0
    ids_ordenados = acrescenta_ids_ordenados(size)

    if crescente:
        for i in range(1, size):
            chave = listdic[ids_ordenados[i]][campo]
            j = i-1

            while j >= 0 and chave < listdic[ids_ordenados[j]][campo]:
                aux = ids_ordenados[j]
                ids_ordenados[j] = ids_ordenados[j + 1]
                ids_ordenados[j + 1] = aux
                j -= 1
    else:
        for i in range(1, size):
            chave = listdic[ids_ordenados[i]][campo]
            j = i-1

            while j >= 0 and chave > listdic[ids_ordenados[j]][campo]:
                aux = ids_ordenados[j]
                ids_ordenados[j] = ids_ordenados[j + 1]
                ids_ordenados[j + 1] = aux
                j -= 1

    return ids_ordenados


def ocultar_senha():
    username = input('username: ')
    password = getpass('password: ')
    return username, password
      


if __name__ == '__main__':
    
    PATH = dirname(__file__)

    # Autenticação
    # username = input('username: ')
    # password = input('password: ')
    username, password = ocultar_senha()


    # puxando arquivo para autenticação
    verifica_cria_arquivo(f"{PATH}/../data/usuario.txt", "root\n123456")

    # Criando a autenticação. Primeiro, vamos extrair o login e senha corretos
    # do arquivo, em seguida tirar o '\n' do login.
    # Depois vamos comparar as variáveis username e password
    # com a do arquivo e não permiti rpassar para a próxima estrutura
    # do programa enquanto não informar o username e password corretos.
    # Para realizar a verificação foi posto um while.

    # vai ser um read, "r", pois queremos extrair informações desse txt
    with open(f"{PATH}/../data/usuario.txt", "r") as arquivo:
        login_info = arquivo.readlines()

    # aqui, vamos estar tirando, ou deletando o '\n'
    login_info[0] = login_info[0].replace('\n', '')

    # fazendo a estrutura que não vai permitir continuar enquanto o username
    # ou o password forem incorretos- pedindo para reescrever ambos
    # se pelo menos um estiver incorreto

    while username != login_info[0] or password != login_info[1]:
        print('username ou password invalidos. Tente novamente.')
        username, password = ocultar_senha()

    print(f'\nOlá, {username}!\n\n')

    # Quando iniciar o programa, já tem de puxar dos dados persistidos em
    # produtos.txt

    tem_prod_txt = verifica_cria_arquivo(
        f"{PATH}/../data/produtos.txt", "id,nome,descricao,peso,valor,fornecedor\n")
    tem_next_txt = verifica_cria_arquivo(f"{PATH}/../data/next_id.txt", "0")
    tem_qtdprod_txt = verifica_cria_arquivo(f"{PATH}/../data/qtd_prod.txt", "0")

    if ((not tem_prod_txt) and tem_next_txt and tem_qtdprod_txt):
        with open(f"{PATH}/../data/next_id.txt", "w") as arquivo:
            arquivo.write("0")
        with open(f"{PATH}/../data/qtd_prod.txt", "w") as arquivo:
            arquivo.write("0")

    with open(f"{PATH}/../data/next_id.txt", "r") as arquivo:
        next_id = int(arquivo.read())
    with open(f"{PATH}/../data/qtd_prod.txt", "r") as arquivo:
        qtd_produtos = int(arquivo.read())

    produtos = []
    produtos = cria_listdicio_com_csv(f"{PATH}/../data/usuario.txt")

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

        # navegando pelo menu

        match resp:
            case 1:
                for i in range(qtd_produtos):
                    print(f'{produtos[i]}\n')
            case 2:
                # colocando uma lista de ids, a qual vamos ordenar
                # (em oposição a alterar a lista de produtos em si)
                # segundo a ordem alfabetica.

                print(
                    "MÉTODOS\n(a) - Bubble sort\n(b) - Insertion sort\n(c) - Selection sort\nEscolha o método: ")
                metodo = input()

                print("ORDEM\n(d) - crescente\n(e) - decrescente\nescolha a ordem:")
                ordem = input()

                print(
                    "COLUNA\n(f) - id\n(g) - nome\n(h) - descricao\n(i) - peso\n(j) - valor\n(k) - fornecedor\nescolha a ordem:")
                coluna = input()

                if ordem == 'd':
                    crescente = 1
                else:
                    crescente = 0

                match coluna:
                    case 'f':
                        campo = 'id'
                    case 'g':
                        campo = 'nome'
                    case 'h':
                        campo = 'descricao'
                    case 'i':
                        campo = 'peso'
                    case 'j':
                        campo = 'valor'
                    case 'k':
                        campo = 'fornecedor'

                match metodo:
                    case 'a':
                        bubble_sort_listdic(produtos, campo, crescente)
                    case 'b':
                        insertion_sort_listdic(produtos, campo, crescente)
                    case 'c':
                        selection_sort_listdic(produtos, campo, crescente)

                ids_ordenados = bubble_sort_listdic(produtos, "nome", 0)

                for i in range(qtd_produtos):
                    print(produtos[ids_ordenados[i]])

            case 3:
                produtos.append({})

                # tem o problema, pois não et

                print('\n')
                produtos[next_id]['id'] = next_id
                produtos[next_id]['nome'] = input('Digite o nome do produto: ')
                produtos[next_id]['descricao'] = input(
                    'Digite a descrição do produto: ')
                produtos[next_id]['peso'] = input('Digite a peso do produto: ')
                produtos[next_id]['valor'] = input(
                    'Digite a valor do produto: ')
                produtos[next_id]['fornecedor'] = input(
                    'Digite a fornecedor do produto: ')

                with open(f"{PATH}/../data/produtos.txt", "a") as arquivo:
                    arquivo.write(f'{produtos[next_id]["id"]}, {produtos[next_id]["nome"]}, {produtos[next_id]["descricao"]}, {
                                  produtos[next_id]["peso"]}, {produtos[next_id]["valor"]}, {produtos[next_id]["fornecedor"]}\n')

                qtd_produtos += 1
                next_id += 1

                with open(f"{PATH}/../data/next_id.txt", "w") as arquivo:
                    arquivo.write(f"{next_id}")
                with open(f"{PATH}/../data/qtd_prod.txt", "w") as arquivo:
                    arquivo.write(f"{qtd_produtos}")

                print('\n')
            case 4:
                with open(f"{PATH}/../data/produtos.txt", "r") as arquivo:
                    temp_info_produtos_txt = arquivo.readlines()

                querAlterarProdutos = 's'
                while querAlterarProdutos == 's':
                    edit_idx = int(
                        input('Digite o id do produto que deseja editar: '))
                    querEditarCampoDoProduto = 's'
                    while querEditarCampoDoProduto == 's':

                        field = input('Digite o campo que deseja editar:')
                        produtos[edit_idx][field] = input(
                            'Digite o novo valor: ')
                        # Aqui, vamos alterar um item específico da lista. Vamos usar o
                        # readlines para deixar todas as informações de um produto
                        # associadas a um índice na lista. Em seguida, vamos alterar
                        # o produto cujo índice é igual a edit_idx. Depois usar write
                        # para devolver ao arquivo

                        atualiza_registros_em_produto_txt(
                            f"{PATH}/../data/produtos.txt", produtos, qtd_produtos)

                        querEditarCampoDoProduto = input(
                            'Deseja continuar alterando esse produto? (Resposta: s/n)')
                    querAlterarProdutos = input(
                        'Deseja continuar alterando produtos? (Resposta: s/n)')

            case 5:
                del_idx = int(
                    input('Digite o id do produto que deseja excluir: '))
                del produtos[del_idx]

                qtd_produtos -= 1
                with open(f"{PATH}/../data/qtd_prod.txt", "w") as arquivo:
                    arquivo.write(f'{qtd_produtos}')

                next_id -= 1
                with open(f"{PATH}/../data/next_id.txt", "w") as arquivo:
                    arquivo.write(f'{next_id}')

                produtos = reordena_ids(produtos, qtd_produtos)

                atualiza_registros_em_produto_txt(
                    f"{PATH}/../data/produtos.txt", produtos, qtd_produtos)
