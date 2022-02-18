n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]

tmp = min(c[0])
a = [0]*n
a[0] = tmp
b = [0]*n
for j in range(n):
    d[0][j] = tmp
    dis = c[0][j]-d[0][j]
    for i in range(n):
        d[i][j] += dis
    b[j] = dis

for i in range(1, n):
    dis = c[i][0]-d[i][0]
    for j in range(n):
        d[i][j] += dis
    a[i] = dis

if c == d:
    print("Yes")
    print(*a)
    print(*b)
else:
    print("No")
