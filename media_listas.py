lista = [1,2,3,4,5,6,7,8,9,10]

count = 0
for count in lista:
    count += 1
print(f"A lista tem um total de {count} números")

soma_da_lista = 0

for num in lista:
    soma_da_lista += num

print(f"A soma de todos os números da lista é {soma_da_lista} ")

media_lista = soma_da_lista / count
print(f"A média da lista é {media_lista:.3}")