AMARELO = "\033[1;33m"
VERMELHO = "\033[0;31m"
AZUL = "\033[0;34m"
RESET = "\033[0m"

### CREATED ###

nomes_lista = []
numero_camisa_lista = []
while True:
    if len(nomes_lista) <= 20:

        nome_jogador = input('\nNome do jogador: ')
        while nome_jogador.isnumeric():
            print(f'{VERMELHO}Nome invalido, digite um nome com caracteres de LETRAS!{RESET}')
            nome_jogador = input('\nNome: ')
        nomes_lista.append(nome_jogador)

        num_camisa = input('Numero da camisa: ')
        while not num_camisa.isnumeric():
            print(f'{VERMELHO}Numero invalido, digite um NUMERO!{RESET}')
            num_camisa = input('Numero da camisa: ')
        numero_camisa_lista.append(num_camisa)
        print(f'\nTemos {len(nomes_lista)}/20 jogadores na lista.\nDeseja adicionar outro nome?')
        condisao = input(f'\n{AMARELO}Pressione qualquer tecla para sair.\n[S] para continuar.{RESET}\-> ').upper()
        if condisao != "S":
            break
    else:
        break

### UPDATE ###

dicionario_jogadores = {}
for jogador, numero in zip(nomes_lista, numero_camisa_lista):
    dicionario_jogadores.update({jogador: numero})


### READ ###

for key in dicionario_jogadores.keys(): print(f'{AZUL}Jogador:{RESET} {key} -> Camisa: {dicionario_jogadores[key]}')


### DELETE ###

print(dicionario_jogadores.clear())
