while True:
    condicao = input('''\nMETODOS\n(a) - Bubble sort\n(b) - Insertion sort\n(c) - Selection sort\n\nEscolha o metodo -> [a,b,c]: ''')
    condicao = condicao.upper()
    if (condicao == 'A') | (condicao == 'B') | (condicao == 'C'):
        break