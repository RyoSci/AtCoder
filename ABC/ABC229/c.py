import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, w = map(int, input().split())
nowa = 0
nowb = 0
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(reverse=True)

for i in range(n):
    a, b = ab[i]
    if nowb == w:
        break
    tmp = min(w-nowb, b)
    nowa += a*tmp
    nowb += tmp

print(nowa)
