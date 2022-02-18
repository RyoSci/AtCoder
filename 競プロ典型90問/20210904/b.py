import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
total = sum(a)

r = 0
now = a[0]
ans = "No"
for l in range(n):
    while 1:
        if now*10 == total:
            ans = "Yes"
            break
        elif now*10 < total:
            r += 1
            now += a[r % n]
        else:
            now -= a[l]
            break

print(ans)
