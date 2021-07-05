n, k = map(int, input().split())
_ = list(map(int, input().split()))

a = []
for i in range(n):
    a.append([_[i], i])

a.sort()

k_ = k % n
res = k//n

ans = [0]*n

for i in range(n):
    if i+1 <= k_:
        ans[a[i][1]] = res+1
    else:
        ans[a[i][1]] = res

for i in range(n):
    print(ans[i])
