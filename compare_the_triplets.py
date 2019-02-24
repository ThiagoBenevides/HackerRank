a=(5,6,7)
b=(3,6,10)
bob=0
ana=0
for i in range(3):
    if a[i]>b[i]:
        bob+=1
    elif a[i]<b[i]:
        ana+=1
    else:
        bob+=0
        ana+=0

print(bob,ana)
