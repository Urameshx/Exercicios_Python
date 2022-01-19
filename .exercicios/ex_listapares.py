lista_pares = [[]]
lista_completa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista_completa:
    if i % 2 == 0:
        lista_pares[0].append(i)

print(lista_pares)

