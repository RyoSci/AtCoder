n, t = map(int, input().split())
res = 1000 + 1
for i in range(n):
    ci, ti = map(int, input().split())
    if ti <= t:
        res = min(res, ci)

if res == 1001:
    print("TLE")
else:
    print(res)