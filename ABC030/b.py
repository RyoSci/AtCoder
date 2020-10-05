n, m = map(int, input().split())
n = n % 12
sita = (60 * n - 11 * m) / 2
print(min(abs(sita), 360 - abs(sita)))
