nome = input('Digite o nome: ').strip().upper()

senha = input('Digite uma senha alfabética: ').strip().upper()

while nome in senha:
    print('DIGITE UMA SENHA DIFERENTE DO NOME!!')
    nome = [input('Digite o nome: ').strip().upper()]
    senha = [input('Digite uma senha alfabética: ').strip().upper()]