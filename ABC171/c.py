n=int(input())
res=""
while n!=0:
    mod=(n-1)%26
    n=(n-1)//26
    # if mod==0:
    #     mod=26
    #     n-=1
    res+=chr(97+mod)
print(res[::-1])