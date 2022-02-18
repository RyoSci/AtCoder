n = int(input())
d = list(map(int, input().split()))
d.sort()
n //= 2

if d[n - 1] == d[n]:
    print(0)
else:
    print(d[n] - d[n - 1])