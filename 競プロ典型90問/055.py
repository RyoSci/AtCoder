n, p, q = map(int, input().split())
a = list(map(int, input().split()))
# n, p, q = 100, 10**9, 10**8
# a = [10**9]*n
res = 0
for i in range(n-4):
    for j in range(i+1, n-3):
        for k in range(j+1, n-2):
            for l in range(k+1, n-1):
                for m in range(l+1, n):
                    if a[i] % p*a[j] % p*a[k] % p*a[l] % p*a[m] % p == q:
                        res += 1
print(res)
