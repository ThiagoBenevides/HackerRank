arr=[1, 2, 3, -1, -2, -3, 0, 0]
num=8
countp=0
countn=0
countz=0
lista=[]

for i in range(num):
    if arr[i]<0:
        countn+=1
    elif arr[i]>0:
        countp+=1
    else:
        countz+=1

fracp= countp/num
fracn=countn/num
fracz=countz/num

fracpformat= format(fracp,'.6f')
fracnformat= format(fracn,'.6f')
fraczformat= format(fracz,'.6f')
print(fracpformat)
print(fracnformat)
print(fraczformat)
