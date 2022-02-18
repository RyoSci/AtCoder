a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

res = a * s + b * t
if s + t >= k:
    res -= c * (s + t)

print(res)
