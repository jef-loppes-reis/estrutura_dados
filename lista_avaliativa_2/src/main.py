def metodos():
    while True:
        condicao = input('''\nMETODOS\n(a) - Bubble sort\n(b) - Insertion sort\n(c) - Selection sort\n\nEscolha o metodo -> [a,b,c]: ''')
        condicao = condicao.upper()
        if (condicao == 'A') | (condicao == 'B') | (condicao == 'C'):
            break
    return condicao


def ordem():
    while True:
        condicao = input('''ORDEM\n(d) - Crescente\n(e) - Decrescente\n\nEscolha a ordem -> [d,e]: ''')
        condicao = condicao.upper()
        if condicao.upper() == 'D' or condicao.upper() == 'E':
            break
    return condicao


def coluna():
    while True:
        condicao = input('''COLUNA\n(f) - id\n(g) - descricao\n(h) - peso\n(i) - valor\n(j) - fornecedor\n\nEscolha a ordem -> [f,g,h,i,j]''')
        condicao = condicao.upper()
        if condicao == 'F' or condicao == 'G' or condicao == 'H' or condicao == 'I' or condicao == 'J':
            break
    return condicao


if __name__ == "__main__":
    