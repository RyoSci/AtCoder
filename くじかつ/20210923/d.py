import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h, w, a, b = map(int, input().split())
res = []

for i in range(h):
    if i < b:
        res.append(list("1"*a+"0"*(w-a)))
    else:
        res.append(list("0"*a+"1"*(w-a)))

for i in range(h):
    print(*res[i], sep="")
