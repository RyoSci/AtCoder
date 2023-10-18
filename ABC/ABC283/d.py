# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
n = len(s)

pre = []
box = [0]*26
alpha_pos = [[] for _ in range(26)]

for i in range(n):
    if s[i] == '(':
        pre.append(i)
    elif s[i] == ')':
        now_pre = pre.pop()
        for j in range(26):
            l = bisect_left(alpha_pos[j], now_pre)
            r = bisect_left(alpha_pos[j], i)
            cnt = r-l
            box[j] -= cnt
            box[j] = max(0, box[j])
    else:
        now = ord(s[i]) - ord('a')
        if box[now] > 0:
            print("No")
            exit()
        else:
            box[now] += 1
            alpha_pos[now].append(i)

print("Yes")
