n, m = map(int, input().split())

res = min(n, m//2)
n -= res
m -= res*2

res += m//4

print(res)
