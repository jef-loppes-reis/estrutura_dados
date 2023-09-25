####### CRETED #######
 
# Abrindo arquivo TXT, com uma lista ofical de paises.
# Fonte: https://www.bcb.gov.br/ftp/paises.txt
with open('../data/lista_de_paises_completa.txt') as archive:
    lista_de_paises_completa = archive.read()

# Slice sobre a lista, para separar os items em '\n' (Paragrafos)
lista_de_paises_completa = lista_de_paises_completa.split('\n')

# Sobre o resultado anterior, outro Slice para quebrar a ',' (virgula)
lista_de_paises_completa = list(map(lambda x: x.split(',')[0], lista_de_paises_completa))

# Sobre o resultado anterior, outro Slice para quebrar o " " (Espacos)
# Por fim, pegando o ultimo item de cada lista, resultando no nome de cada pais.
lista_de_paises_completa = list(map(lambda x: x.split(' ')[-1], lista_de_paises_completa))

contagem_paises = {
    1: 'Primeiro',
    2: 'Segundo',
    3: 'Terceiro',
    4: 'Quarto',
    5: 'Quinto',
    6: 'Sexto',
    7: 'Setimo',
    8: 'Oitavo',
    9: 'Nono',
    10: 'Decimo'
    }

lista_paises_saida = []

####### READ #######
print(' Liste 10 paises de escolha '.center(50,'*'))
for x in range(1,11):
    lista_paises_saida.append(input(f'\nDigite o {contagem_paises[x]}:'))
    # system('cls')
    print(dict(enumerate(lista_paises_saida,1)))


####### UPDATE #######


####### DELETE #######
for x in range(1,11):
    while True:
        indicador = input("\nDigite o numero indicador, para deletar um pais da lista: ")
        if indicador.isnumeric():
            lista_paises_saida.pop(indicador)
            print(f'\nPais com o indicador numero {indicador} foi deletado!\n')
            print(lista_paises_saida)
