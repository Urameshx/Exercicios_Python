def lista_impar(lista):
    aux = []               # lista auxiliar para armazenar os números impares
    for i in lista:
        if i % 2 != 0:
            aux.append(i)
    return print(f'Os números impares dessa lista são {aux}')

notas = [1,2,3,4,5,6,7,8,9,10]
lista_impar(notas)

