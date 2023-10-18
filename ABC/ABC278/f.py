# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)

memo = dict()


def f(i, pre=-1):
    if (i, pre) in memo:
        return memo[(i, pre)]

    if i == 0:
        return False

    win = False
    for j in range(n):
        if i >> j & 1:
            if pre == -1 or s[pre][-1] == s[j][0]:
                if f(i-(1 << j), j) == False:
                    win = True

    memo[(i, pre)] = win
    return memo[(i, pre)]


if f((1 << n) - 1):
    print("First")
else:
    print("Second")
