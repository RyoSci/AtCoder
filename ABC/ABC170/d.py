n=int(input())
a=list(map(int,input().split()))
a.sort()

if n==1:
    print(1)
elif len(set(a))==1:
    print(0)
elif 1 in a:
    print(1)
else:
    counter=0
    for i in range(len(a)):
        for j in (range(i)):
            if a[i]%a[j]==0:
                break
        else:
            counter+=1
    print(counter)