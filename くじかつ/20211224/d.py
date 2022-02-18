import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x, y = list(map(int, input().split()))
ans = [0]*n
for i in range(1, n):
    for j in range(i+1, n+1):
        if i < y:
            dis = min(abs(i-x)+1+abs(j-y), j-i)
        else:
            dis = j-i
        ans[dis] += 1

print(*ans[1:], sep="\n")
