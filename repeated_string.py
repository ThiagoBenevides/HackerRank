string='aba'
n=10
count=0
count2=0

if len(string)==1:
    if string[0]=='a':
        print(n)
    elif string[0]!='a':
        print(0)
else:
    for i in range(len(string)):
        if string[i]=='a':
            count+=1

    quociente= n//len(string)
    resto= n%len(string)


    for i in range(resto):
        if string[i]=='a':
            count2+=1

    parcial= quociente*count
    num_a= parcial+count2

    print(num_a)
