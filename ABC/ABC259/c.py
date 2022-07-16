# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
t = input()

n = len(s)
m = len(t)

sl = []
tl = []

tmp = s[0]
for i in range(n-1):
    if s[i] != s[i+1]:
        sl.append(tmp)
        tmp = s[i+1]
    else:
        tmp += s[i]
sl.append(tmp)

tmp = t[0]
for i in range(m-1):
    if t[i] != t[i+1]:
        tl.append(tmp)
        tmp = t[i+1]
    else:
        tmp += t[i]
tl.append(tmp)

# print(sl)
# print(tl)

if len(sl) != len(tl):
    print("No")
else:
    n = len(sl)
    ans = "Yes"
    for i in range(n):
        if len(sl[i]) == 1:
            if sl[i] == tl[i]:
                continue
            else:
                ans = "No"
        else:
            if sl[i][0] == tl[i][0] and len(sl[i]) <= len(tl[i]):
                continue
            else:
                ans = "No"
    print(ans)
