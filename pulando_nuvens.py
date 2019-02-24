n=6
nuvens=[0,0,0,1,0,0]
salto=0
conta=0
fim= n-1

while conta<fim:
    if((conta+2)<= fim) and (nuvens[conta+2]==0):
        conta+=2
        salto+=1
    elif nuvens[conta+1]==0:
        conta+=1
        salto+=1

print(salto)
