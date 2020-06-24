k,n=map(int,input().split())
a=[int(i) for i in input().split()]
array=[]
result=a[n-1]-a[0]
array.append(result)
for i in range(1,n):
    result=k+a[i-1]-a[i]
    array.append(result)
print(min(array))

###################################
len_array=[]
for i in range(n):
    if i==n-1:
        length=a[0]-a[i]+k
    else:
        length=a[i+1]-a[i]
    len_array.append(length)  
# len_array.index(max(len_array))
print(sum(len_array)-max(len_array))
###################################