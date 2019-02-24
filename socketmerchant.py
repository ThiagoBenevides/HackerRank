#-*- coding: utf-8 -*-
lista = [10, 20, 20, 10, 10, 30, 50, 10, 20]

total = []
contagem = []
pares_socket=[]
for ocorrencia in lista:
    if total.count(ocorrencia) == 0:
	       total.append(ocorrencia)
	       contagem.append(lista.count(ocorrencia))


for i in range(len(contagem)):
    pares= contagem[i]//2;
    pares_socket.append(pares)
soma=sum(pares_socket)
print("O número de pares formados é de: {}".format(soma))
