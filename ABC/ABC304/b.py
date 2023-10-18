# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

if n <= 10**3-1:
    ans = n
elif n <= 10**4-1:
    ans = n//10*10
elif n <= 10**5-1:
    ans = n//100*100
elif n <= 10**6-1:
    ans = n//1000*1000
elif n <= 10**7-1:
    ans = n//10000*10000
elif n <= 10**8-1:
    ans = n//100000*100000
elif n <= 10**9-1:
    ans = n//1000000*1000000

print(ans)
