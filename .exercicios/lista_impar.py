def lista_impar(lista):
    count = 0
    for i in lista:
        if lista[i] % 2 == 1:
            count += 1
    return print(f'Essa lista tem {count} números impares')


lista_impar([2, 1, 2, 3, 4])

'''lista_de_numeros=[2,1,2,3,4]
i=0
j=0
for i in range(len(lista_de_numeros)):
  if (lista_de_numeros[i]) % 2 != 0 :
    j=j+1
print(j)'''
