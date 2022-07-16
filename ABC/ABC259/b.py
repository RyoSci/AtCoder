# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import math
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b, d = list(map(int, input().split()))

sita = math.radians(d)
x = math.cos(sita)
y = math.sin(sita)

c = complex(x, y)
t = complex(a, b)

t *= c
print(t.real, t.imag)
