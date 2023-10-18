# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

call = [0]*n
for i in range(n):
    if call[i]:
        continue
    call[a[i]-1] = 1

ans = []
for i in range(n):
    if call[i] == 0:
        ans.append(i+1)

print(len(ans))
print(*ans)
