import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))

t_confirm = [1]*n
a_confirm = [1]*n

for i in range(n-1):
    if t[i] == t[i+1]:
        t_confirm[i+1] = 0

for i in range(n-1, 0, -1):
    if a[i] == a[i-1]:
        a_confirm[i-1] = 0

ans = [1]*n

for i in range(n):
    if t_confirm[i] & a_confirm[i]:
        if t[i] != a[i]:
            ans[i] = 0
            break
    elif t_confirm[i] and not a_confirm[i]:
        if t[i] > a[i]:
            ans[i] = 0
            break
    elif not t_confirm[i] and a_confirm[i]:
        if t[i] < a[i]:
            ans[i] = 0
            break
    else:
        ans[i] = min(t[i], a[i])


res = 1
mod = 10**9+7
for i in range(n):
    res *= ans[i]
    res %= mod
print(res)
