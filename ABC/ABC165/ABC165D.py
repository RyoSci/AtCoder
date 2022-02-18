a,b,n=map(int,input().split())
res=0
x=n
for x in range(min(1000001,b,n+1)):
    res=max(res,int(a*x/b)-a*int(x/b))
res=max(res,int(a*n/b)-a*int(n/b))    
print(res)