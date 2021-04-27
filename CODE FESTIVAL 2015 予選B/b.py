n, m = map(int, input().split())
a = list(map(int, input().split()))
cnts = [0] * (m + 1)
for i in range(n):
    cnts[a[i]] += 1

if max(cnts) > n // 2:
    print(cnts.index(max(cnts)))
else:
    print("?")
