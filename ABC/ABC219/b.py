import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = [input().strip() for _ in range(3)]
t = input().strip()

ans = ""
for i in t:
    ans += s[int(i)-1]

print(ans)
