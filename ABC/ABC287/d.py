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

cnt = 0
match = [0]*m
for i in range(m):
    if s[-m+i] == t[i]:
        cnt += 1
        match[i] = 1
    elif s[-m+i] == "?" or t[i] == "?":
        cnt += 1
        match[i] = 1
    else:
        match[i] = 0

if cnt == m:
    print("Yes")
else:
    print("No")

for i in range(m):
    if match[i]:
        cnt -= 1

    if s[i] == t[i]:
        cnt += 1
    elif s[i] == "?" or t[i] == "?":
        cnt += 1

    if cnt == m:
        print("Yes")
    else:
        print("No")
