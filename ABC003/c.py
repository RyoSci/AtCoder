n, k = map(int, input().split())
r = sorted(list(map(int, input().split())), reverse=True)
res = 0
for i in range(k):
    res = (res + r[k - 1 - i]) / 2
print(res)
