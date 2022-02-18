def factorization(n):
    counter_map={}
    i=2
    tmp=1
    flag=True
    while n!=1:
        #因数に持つか判定
        if n%i==0:
            flag=False
            n=n//i
            #素数判定
            for j in range(2,int(i**(1/2))+1):
                if i%j==0:
                    break
            else:
                tmp*=i
                if i not in counter_map:
                    counter_map[i]=1
                    tmp=1
                else:
                    if tmp not in counter_map:
                        counter_map[tmp]=1
                        tmp=1
        else:
            i+=1
            tmp=1
            flag=True
        if i>int(n**(1/2))+1 and n!=1 and flag:
            counter_map[n]=1
            break
        print(i,n,counter_map)
    return counter_map


a=int(input())
b=factorization(a)
print(b)
# sum=0

# for i in b.keys():
#     counter=0
#     for j in range(1,41):
#         if b[i]>=1+(j+2)*(j-1)//2:
#             counter=j
#         else:
#             break
#     sum+=counter

# print(sum)

print(len(b))
