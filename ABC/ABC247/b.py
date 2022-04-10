# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = []
t = []
for i in range(n):
    si, ti = input().split()
    s.append(si)
    t.append(ti)

ans = True
for i in range(n):
    flag = True
    flag1 = True
    for j in range(n):
        if i == j:
            continue
        if s[i] == s[j] or s[i] == t[j]:
            flag = False
        if t[i] == s[j] or t[i] == t[j]:
            flag1 = False
    if flag == False and flag1 == False:
        ans = False

if ans:
    print("Yes")
else:
    print("No")
