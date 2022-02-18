n, q = map(int, input().split())
a = [0]+list(map(int, input().split()))+[10**19]
query = []
for i in range(q):
    query.append([int(input()), i])
query.sort()

ans = []
j = 0
for i in range(n+1):
    l = a[i]
    r = a[i+1]
    while j < q:
        ki = query[j]
        if r <= ki[0]+i:
            break
        elif l < ki[0]+i < r:
            ans.append([ki[1], ki[0]+i])
            j += 1

ans.sort()

for i in range(q):
    print(ans[i][1])
