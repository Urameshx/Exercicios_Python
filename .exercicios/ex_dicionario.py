aluno = dict()
aluno['nome'] = input('Digite um nome: ')
aluno['media'] = float(input(f'A media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for i,j in aluno.items():
    print(f'{i} é igual a {j}')