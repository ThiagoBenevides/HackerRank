num=3
principal=0
secundaria=0

arr=[[11,2,4],
    [4,5,6],
    [10,8,-12]
]
print(len(arr))
for linha in range(3):
    for coluna in range(3):
        if linha==coluna:
            principal+=arr[linha][coluna]


for linha in range(num):
    for coluna in range(num):
        if linha ==num-1-coluna:
            secundaria+= arr[linha][coluna]

soma= principal-secundaria

if soma<0:
    print(soma*(-1))
else:
    print(soma)
