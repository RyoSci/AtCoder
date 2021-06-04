n, k, s = map(int, input().split())
if s == 10**9:
    res = [s]*k + [s-1]*(n-k)
else:
    res = [s]*k + [s+1]*(n-k)

print(*res)
