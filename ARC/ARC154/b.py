# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()
t = input()

if sorted(s) != sorted(t):
    print(-1)
    exit()


def f(x):
    i = x
    j = 0
    while i < n:
        if j == n:
            return False
        while j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
                break
            j += 1

    return True


ok = n-1
ng = -1
while ng+1 < ok:
    m = (ng+ok)//2
    if f(m):
        ok = m
    else:
        ng = m

print(ok)
