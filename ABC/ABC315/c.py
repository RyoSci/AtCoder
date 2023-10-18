# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
fs = []

for i in range(n):
    f, s = map(int, input().split())
    fs.append((s, f))

fs.sort(reverse=True)

first = fs[0]
ans = 0
for second in fs[1:]:
    if first[1] == second[1]:
        ans = max(ans, first[0] + second[0]//2)
    else:
        ans = max(ans, first[0] + second[0])

print(ans)
