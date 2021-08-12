n, k = map(int, input().split())

res = min(n % k, abs(k-n % k))
print(res)
