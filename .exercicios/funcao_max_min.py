def dif_max_min(lista):
    menor = min(lista)
    maior = max(lista)
    res = maior - menor
    return res

notas = [2,10,7,2]
print (dif_max_min(notas))

