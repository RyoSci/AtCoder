import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
s = input().split()
t = set(input().split())

ans = []
for si in s:
    if si in t:
        ans.append("Yes")
    else:
        ans.append("No")


print(*ans, sep="\n")
