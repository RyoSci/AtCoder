# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18

s = input().split()
t = input().split()

cnt = 0
for i in range(3):
    if s[i] == t[i]:
        cnt += 1

if cnt == 3 or cnt == 0:
    print("Yes")
else:
    print("No")
