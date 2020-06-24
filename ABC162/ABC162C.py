import math
a=int(input())
counter=0
for i in range(1,a+1):
    for j in range(1,a+1):
        tmp=math.gcd(i,j)
        for k in range(1,a+1):
            counter+=math.gcd(tmp,k)
print(counter)

#######################################
a=int(input())
counter=0
for i in range(1,a+1):
    for j in range(i,a+1):
        for k in range(j,a+1):
            if i==j and j==k:
                times=1
            elif i!=j and j!=k and k!=i:
                times=6 
            else:
                times=3
            
            for l in range(i,0,-1): 
                if i%l==0 and j%l==0 and k%l==0:
                    counter+=(l*times)
                    break
print(counter)