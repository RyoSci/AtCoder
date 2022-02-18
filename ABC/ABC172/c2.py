import typing

def binary_serch(x:int, b_sum:list):
    l = 0
    r = len(b_sum) - 1
    mid = (l + r + 1) // 2
    res = mid
    while True:
        if x == b_sum[mid]:
            return mid
        elif x < b_sum[mid]:
            res = mid - 1
            r = mid
            mid = (l + r + 1) // 2
        elif b_sum[mid] < x:
            res = mid 
            l = mid
            mid = (l + r + 1) // 2
        if l + 1 == r:
            return res

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_sum = [0] * (m + 2)
for i in range(m):
    b_sum[i + 1] = b[i] + b_sum[i]

b_sum[-1] = 10 ** 9 + 1
a = [0] + a
pass_k = 0
ans = 0
for i in range(n + 1):
    if pass_k + a[i] <= k:
        pass_k += a[i]
        book = i
        book += binary_serch(k - pass_k, b_sum)
        ans = max(ans, book)
    else:
        break

print(ans)