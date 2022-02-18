import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = input().split()

a = a[::-1]
b = b[::-1]

ans = "Easy"

for i in range(min(len(a), len(b))):
    if int(a[i])+int(b[i]) >= 10:
        ans = "Hard"
        break

print(ans)
