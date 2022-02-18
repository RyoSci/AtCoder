import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

f = 0
t = 0

for i in range(n):
    if a[i] % 4 == 0:
        f += 1
    elif a[i] % 2 == 0:
        t += 1

if n % 2 == 0:
    if 2*f >= n:
        ans = "Yes"
    elif n-2*f <= t:
        ans = "Yes"
    else:
        ans = "No"

else:
    if 2*f+1 >= n:
        ans = "Yes"
    elif n-2*f <= t:
        ans = "Yes"
    else:
        ans = "No"

print(ans)
