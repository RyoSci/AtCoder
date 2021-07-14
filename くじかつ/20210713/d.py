n = int(input())

csf = []
for i in range(n-1):
    c, s, f = map(int, input().split())
    csf.append([c, s, f])

for i in range(n):
    x = 0
    for j in range(i, n-1):
        c, s, f = csf[j]
        x = s+max(0, x-s+f-1)//f*f+c
    print(x)
