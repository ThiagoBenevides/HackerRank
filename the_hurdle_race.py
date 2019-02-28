n=5
k=4
lista=[1,6,3,5,2]
lista.sort(reverse=True)

if lista[0]<k:
    print('Zero')
else:
    minimo=lista[0]-k
    print(minimo)
