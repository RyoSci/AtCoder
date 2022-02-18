import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

ans = h[0]
for i in range(1, n):
    if ans < h[i]:
        ans = h[i]
    else:
        break

print(ans)
