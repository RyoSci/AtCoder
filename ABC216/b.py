import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
st = [input().split() for _ in range(n)]

ans = "No"
for i in range(n-1):
    for j in range(i+1, n):
        if st[i] == st[j]:
            ans = "Yes"
            break

print(ans)
