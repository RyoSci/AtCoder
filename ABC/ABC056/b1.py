w, a, b = map(int, input().split())
res = max(0, abs(a - b) - w)
print(res)
