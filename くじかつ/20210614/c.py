n, q = map(int, input().split())
a = [0]+list(map(int, input().split()))+[10**19]

query = []
for i in range(q):
    query.append([int(input()), i])

query.sort()

j = 0
ans = []
for i in range(n+1):
    l = a[i]
    r = a[i+1]
    while j < q:
        k = query[j]
        if l < k[0]+i < r:
            j += 1
            ans.append([k[1], k[0]+i])
        else:
            break

ans.sort()
for i in ans:
    print(i[1])
