# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

d = [range(1, 10)]
a = [51, 3, 44, 99, 1, 87, 83, 19, 10, 90]
b = [720, 477, 230, 77, 19, 5, 4, 0, 0, 0]

a_tot = sum(a)
b_tot = sum(b)

print(a_tot, b_tot)
for i in range(10):
    print(a[i]/a_tot, b[i]/b_tot)
