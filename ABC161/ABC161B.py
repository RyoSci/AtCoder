n,m=map(int,input().split())
num=[int(i) for i in input().split()]
num=sorted(num,reverse=True)
sum_num=sum(num)
for i in range(m):
    if num[i]<sum_num/(4*m):
        print("No")
        break
else:
    print("Yes")