n,m,x=map(int,input().split())
price_points=[]
for i in range(n):
    line=list(map(int,input().split()))
    price_points.append(line)
sum_list=[]
for i in range(2**n):
    i=bin_str = format(i, 'b')
    # i=str(i)
    i_len=len(i)
    i_n_bit="0"*(n-i_len)+i
    sum_=0
    points=[0]*m
    print(i_n_bit)
    for j in range(n):
        if i_n_bit[j]=="0":
            continue
        else:
            sum_+=price_points[j][0]
            for k in range(m):
                points[k]+=price_points[j][k+1]
    counter=0
    for l in range(m):
        if points[l]>=x:
            counter+=1    
    if counter==m:
        sum_list.append(sum_)
if len(sum_list)==0:
    print(-1)
else:
    print(min(sum_list))