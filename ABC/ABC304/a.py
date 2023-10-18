# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = []
a = []
for i in range(n):
    si, ai = map(str, input().split())
    s.append(si)
    a.append(int(ai))

pos = 0
for i in range(n):
    if a[pos] > a[i]:
        pos = i

for i in range(n):
    print(s[(pos+i) % n])
