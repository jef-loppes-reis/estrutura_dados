def bubble_sort(lista:list) -> None:
    tamanho = len(lista)
    condicao_troca = False
    for elemento_da_lista in range(tamanho-1):
        for x in range(0, tamanho - elemento_da_lista - 1):
            if lista[x] > lista[x + 1]:
                condicao_troca = True
                lista[x], lista[x + 1] = lista[x + 1], lista[x]
        if not condicao_troca:
            break


def lista_numeros_aleatorios():
    from random import random
    lista_random = []
    for _ in range(10):
        lista_random.append(int(random() * 101))
    return lista_random


if __name__ == '__main__':

    # # Exemplo usando o metodo nativo do Python "SORTED".
    # numeros_aleatorios = lista_numeros_aleatorios()
    # print(f'Lista aleatoria: {numeros_aleatorios}')
    # # sorted(numeros_aleatorios)
    # print(f'Lista ordenada: {sorted(numeros_aleatorios)}')


    # Exemplo usando o metodo criado "bubble_sort".
    numeros_aleatorios = lista_numeros_aleatorios()
    print(f'\nLista aleatoria gerada: {numeros_aleatorios}')
    bubble_sort(numeros_aleatorios)
    print(f'\nBubbleSort: {numeros_aleatorios}\n')
