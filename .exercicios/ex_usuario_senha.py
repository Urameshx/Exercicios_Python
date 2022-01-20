nome = input('Digite o nome: ').strip().upper()
senha = input('Digite uma senha alfabética: ').strip().upper()
print(senha in nome)

while senha in nome:
    print('DIGITE UMA SENHA DIFERENTE DO NOME!!')
    nome = input('Digite o nome: ').strip().upper()
    senha = input('Digite uma senha alfabética: ').strip().upper()
