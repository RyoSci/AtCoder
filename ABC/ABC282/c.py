# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

cnt = 0
ans = []
for i in range(n):
    if s[i] == ",":
        if cnt % 2 == 0:
            ans.append(".")
        else:
            ans.append(s[i])
    elif s[i] == '"':
        cnt += 1
        ans.append(s[i])
    else:
        ans.append(s[i])

print("".join(ans))
