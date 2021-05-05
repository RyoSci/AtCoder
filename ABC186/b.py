h, w = map(int, input().split())

a = []
min_num = 100
for i in range(h):
    ai = list(map(int, input().split()))
    a.append(ai)
    for j in range(w):
        min_num = min(min_num, ai[j])

res = 0
for i in range(h):
    for j in range(w):
        res += a[i][j]-min_num

print(res)
