# n,m,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))

# counter=0
# sum_min=0
# i,j=0,0
# flag = True
# while i<n and j<m:
#     if a[i] <= b[j]:
#         sum_min+=a[i]
#         i+=1
#     else:
#         sum_min+=b[j]
#         j+=1
#     if flag and i==n:
#         a[n-1]=10**9+1
#         i=n-1
#         flag=False
#     if flag and j==m:
#         b[m-1]=10**9+1
#         j=m-1
#         flag=False
#     if sum_min <= k:
#         counter+=1
#     elif sum_min > k:
#         print(counter)
#         break
#     # print(i,j)
#     # print(sum_min)
# else:
#     print(counter)
# # print(sum_min)

#再思考 TLE
n, m ,k = map(int, input(). split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_sum = [0] * (n + 1)
b_sum = [0] * (m + 1)
for i in range(n):
    a_sum[i + 1] = a_sum[i] + a[i]
for i in range(m):
    b_sum[i + 1] = b_sum[i] + b[i]
res = 0
for i in range(n+1):
    for j in range(m+1):
        if a_sum[i] + b_sum[j] <= k:
            res = max(res, i + j)
        else:
            break
print(res)