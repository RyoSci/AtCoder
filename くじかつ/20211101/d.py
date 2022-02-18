import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
csf = [list(map(int, input().split())) for _ in range(n-1)]

ans = []
for i in range(n-1):
    now = 0
    for j in range(i, n-1):
        c, s, f = csf[j]
        if now <= s:
            now = s
            now += c
        else:
            now = s+(now-s+f-1)//f*f
            now += c
    ans.append(now)
ans.append(0)
print(*ans, sep="\n")
