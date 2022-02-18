n=int(input())
a=list(map(int,input().split()))
res=0
for i in a:
    res=res^i

ans=[]
for i in a:
    ans.append(res^i)
print(ans)

