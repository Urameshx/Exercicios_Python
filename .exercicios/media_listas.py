lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for count in lista:
    total = count
print(f'A lista tem um total de {total} números')

soma_da_lista = 0
for num in lista:
    soma_da_lista += num

print(f"A soma de todos os números da lista é {soma_da_lista} ")

media_lista = soma_da_lista / count
print(f"A média da lista é {media_lista:.3}")