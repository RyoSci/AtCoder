# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18


s = input()
ans = ""

for i in s:
    if i not in "aeiou":
        ans+=i

print(ans)