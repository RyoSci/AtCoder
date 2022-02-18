n, m = map(int, input().split())
a = [[i, i] for i in range(n)]
top = 0
for i in range(m):
    top -= 1
    ai = int(input()) - 1
    a[ai][1] = top

a.sort(key=lambda x: x[1])
for i in range(n):
    print(a[i][0] + 1)
