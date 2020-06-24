def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

a=int(input())
b=factorization(a)
#print(b)
sum=0

for i in b:
    counter=0
    for j in range(1,100):
        #print(1+(j+2)*(j-1)//2)
        if i[1]>=1+(j+2)*(j-1)//2:
            counter=j
        else:
            break
    sum+=counter
if a==1:
  print(0)
else:
  print(sum)