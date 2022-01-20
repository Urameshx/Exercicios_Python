meses = ["jan", 'fev', 'março', 'abril', 'maio', 'junho']

temp = [float(input(f'Digite a temp do mês {meses[i]} '))
        for i in range (len(meses))]

print(f'a média foi de {round(sum(temp)/len(temp),2)}')

''' 
import statistics as st
i = 1
lista_temp = []
for i in range(13):
    lista_temp.append(int(input(f'Digite a temperatura do {i}º mês: ')))
    i += 1
print(f'{st.mean(lista_temp):.2f}') 
'''
