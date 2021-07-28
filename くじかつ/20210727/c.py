n = int(input())
a = list(map(int, input().split()))
d = dict()

for i in range(n):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1


ans = []
for key, val in d.items():
    if val >= 4:
        ans.append(key)
        ans.append(key)
    elif val >= 2:
        ans.append(key)

if len(ans) < 2:
    print(0)
else:
    ans.sort(reverse=True)
    print(ans[0]*ans[1])
