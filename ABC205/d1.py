n, q = map(int, input().split())
a = list(map(int, input().split()))+[10**19]
k = [[int(input()), i] for i in range(q)]
k.sort()

ans = []
j = 0
for i in range(q):
    while j < n+1:
        if j+k[i][0] < a[j]:
            ans.append([k[i][1], j+k[i][0]])
            break
        else:
            j += 1

ans.sort()
for i in range(q):
    print(ans[i][1])
