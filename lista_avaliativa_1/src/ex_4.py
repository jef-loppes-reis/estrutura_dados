with open('../data/exemplode_manipulacao_arquivos_ex4.txt', 'w') as archive:
    archive.write(input('\n### Criando arquivo ## \nDigite o texto: \n\t'))

with open('../data/exemplode_manipulacao_arquivos_ex4.txt', 'r') as archive:
    print('\nSeu texto:\n')
    print(archive.read())

with open('../data/exemplode_manipulacao_arquivos_ex4.txt', 'a') as archive:
    archive.write(input('\n### Exemplo de alteracao ###\nDigite um novo texto: \n\t'))

with open('../data/exemplode_manipulacao_arquivos_ex4.txt', 'r') as archive:
    print('\nSeu novo texto: \n\t')
    print(archive.read())

with open('../data/exemplode_manipulacao_arquivos_ex4.txt', 'w') as archive:
    print('\n### LINPANDO ARQUIVO ###')
    archive.write('')

with open('../data/exemplode_manipulacao_arquivos_ex4.txt', 'r') as archive:
    print('\n### Texto Final ###')
    if len(archive.read()) <= 0:
        print('\nArquivo limpo.')
