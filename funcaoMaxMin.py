def dif_max_min(lista):
    menor = min(lista)
    maior = max(lista)
    res = maior - menor
    return res

notas = [2,4,6,8,10]
print (dif_max_min(notas))

