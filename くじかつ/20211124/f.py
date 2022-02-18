import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
rest = 0
for i in range(n):
    if i >= k:
        rest += a[i]


def cal(m, rest):
    for i in range(k):
        if a[i]-m >= 0:
            continue
        rest -= m-a[i]
    if rest >= 0:
        return True
    else:
        return False


l = 0
r = 10**18
while l + 1 < r:
    m = (l+r)//2
    if cal(m, rest):
        l = m
    else:
        r = m


print(l)
