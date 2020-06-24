n=int(input())
num=list(map(int,input().split()))

sum=1
if 0 in num:
    print(0)
else:
    for i in range(n):
        sum*=num[i]
        if sum>10**18:
            print(-1)
            break
    else:
        print(sum)