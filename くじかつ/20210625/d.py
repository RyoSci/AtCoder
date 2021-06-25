n, m = map(int, input().split())
d = dict()

for i in range(m):
    pi, yi = map(int, input().split())
    if pi not in d:
        d[pi] = []
    d[pi].append([yi, i])

ans = [0]*m
for key, val in d.items():
    val.sort()
    for cnt, (yi, i) in enumerate(val):
        ans[i] = [str(key), str(cnt+1)]

for pi, x in ans:
    res = (6-len(pi))*"0"+pi + (6-len(x))*"0"+x
    print(res)
