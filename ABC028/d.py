n, k = map(int, input().split())
res = 0
res += (k - 1) * (n - k) * 6
res += (k - 1) * 3 + (n - k) * 3
res += 1

print(res / (n * n * n))
