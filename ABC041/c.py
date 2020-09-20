n = int(input())
a = [[int(j), i + 1] for i, j in zip(range(n), input().split())]
a.sort(reverse=True)

for i in range(n):
    print(a[i][1])
