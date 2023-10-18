# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

ps = []
for i in range(n):
    if s[i] == "p":
        ps.append(i)

if len(ps) == 0:
    print(s)
else:
    res = [s]
    l = ps[0]
    for r in ps:
        t = s[l:r+1]
        t = t[::-1]
        ft = []
        for i in t:
            if i == "p":
                ft.append("d")
            else:
                ft.append("p")
        ft = "".join(ft)
        ss = s[:l]+ft+s[r+1:]
        res.append(ss)
    res.sort()
    print(res[0])
