class Cores:
    """ ANSI color codes """
    PRETO = "\033[0;30m"
    VERMELHO = "\033[0;31m"
    VERDE = "\033[0;32m"
    MARROM = "\033[0;33m"
    AZUL = "\033[0;34m"
    ROXO = "\033[0;35m"
    CIANO = "\033[0;36m"
    CINZA_CLARO = "\033[0;37m"
    CINZA_ESCURO = "\033[1;30m"
    VERMELHO_CLARO = "\033[1;31m"
    VERDE_CLARO = "\033[1;32m"
    AMARELO = "\033[1;33m"
    AZUL_CLARO = "\033[1;34m"
    ROXO_CLARO = "\033[1;35m"
    CIANO_CLARO = "\033[1;36m"
    BRANCO_CLARO = "\033[1;37m"
    NEGRITO = "\033[1m"
    FAINT = "\033[2m"
    ITALICO = "\033[3m"
    SUBLINHADO = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVO = "\033[7m"
    TRACADO = "\033[9m"
    RESET = "\033[0m"

cor =  Cores()

nomes_lista = []
numero_camisa_lista = []
while True:
    if len(nomes_lista) <= 20:
        nome_jogador = input('\nNome do jogador: ')
        numero_camisa_lista = input('Numero da camisa')
        while nome_jogador.isnumeric():
            print(f'{cor.VERMELHO}Nome invalido, digite um nome com caracteres de LETRAS!{cor.RESET}')
            nome_jogador = input('\nNome: ')
        nomes_lista.append(nome_jogador)
        print(f'\nTemos {len(nomes_lista)}/20 jogadores na lista.\nDeseja adicionar outro nome?')
        condisao = input(f'\n{cor.AMARELO}Pressione qualquer tecla para sair. Ou tecla [S] para continuar.{cor.RESET}').upper()
        if condisao != "S":
            break
    else:
        break

print(nomes_lista)