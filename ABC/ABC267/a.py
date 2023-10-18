# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
s = input()
for i in range(5):
    if s == days[i]:
        print(5-i)
        exit()