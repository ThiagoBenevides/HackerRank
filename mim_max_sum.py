lista=[1,2,3,4,5]
num= len(lista)
soma= sum(lista)
aux=[]

for i in range(num):
    aux.append(soma-lista[i])



minimo=min(aux)
maximo=max(aux)

print(minimo,maximo)
