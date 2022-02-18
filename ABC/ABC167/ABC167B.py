a,b,c,k=map(int,input().split())
a_=min(a,k)
sum_=max(0,k-a)
res=a_*1
b_=min(sum_,b)
sum_=max(0,sum_-b)
res+=b_*0
c_=min(sum_,c)
res+=(-1)*c_
print(res)

