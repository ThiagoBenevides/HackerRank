n=8
s=['U','D','D','D','U','D','U','U']

s1=['U''D''U''U''U''D''U''D''D','D']


contagem=0
vale=0

for i in range(len(s)):
    if s[i]=='U':
        contagem+=1
        if contagem==0:
            vale+=1
    else:
        contagem-=1

print(vale)
