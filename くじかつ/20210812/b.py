n = int(input())
a = list(map(int, input().split()))
s = [0]*n
s[0] = a[0]
for i in range(1, n):
    s[i] += s[i-1]+a[i]

for i in range(1, n):
    s[i] += s[i-1]

max_k = a[0]

for k in range(n):
    max_k = max(max_k, a[k])
    res = max_k*(k+1)+s[k]
    print(res)
