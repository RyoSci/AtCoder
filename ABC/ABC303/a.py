# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()
t = input()

ans = "Yes"
for i in range(n):
    if s[i] == t[i]:
        continue
    elif (s[i] == "1" and t[i] == "l") or (s[i] == "l" or t[i] == "1"):
        continue
    elif (s[i] == "0" and t[i] == "o") or (s[i] == "o" or t[i] == "0"):
        continue
    else:
        ans = "No"

print(ans)
