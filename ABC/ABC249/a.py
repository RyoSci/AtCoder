# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b, c, d, e, f, x = list(map(int, input().split()))

t_dis = x//(a+c)*a*b
t_dis += min(a, x % (a+c))*b

a_dis = x//(d+f)*d*e
a_dis += min(d, x % (d+f))*e

if t_dis == a_dis:
    print("Draw")
elif t_dis > a_dis:
    print("Takahashi")
else:
    print("Aoki")
