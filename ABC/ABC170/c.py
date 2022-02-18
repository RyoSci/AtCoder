x,n=map(int,input().split())
if n ==0:
    print(x)
else:
    p=list(map(int,input().split()))
    tmp=101
    min_num=101
    for i in range(102):
        if i not in p:
            if tmp > abs(x-i):
                min_num=i
                tmp=abs(x-i)
    print(min_num)
