n,down,up=map(int,input().split())
out=0
for i in range(n+1):
    temp_sum=0
    for j in str(i):
        temp_sum+=int(j)
    # print(i,temp_sum)
    if down<=temp_sum and temp_sum<=up:
        out+=i
print(out)