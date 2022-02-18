n, a, b = map(int, input().split())
tmp = min(n, 5)
print(tmp*b+(n-tmp)*a)
