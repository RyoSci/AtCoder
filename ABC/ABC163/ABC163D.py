n,k=map(int,input().split())
sum_num=0
for i in range(k,n+2):
    sum_num+=(i*n-i*(i-1)+1)
    # print(sum_num,i)
print(sum_num%(10**9+7))