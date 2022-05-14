# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q = map(int, input().split())
x = [int(input())-1 for _ in range(q)]

pos2num = [i for i in range(n)]
num2pos = [i for i in range(n)]

for xi in x:
    pos = num2pos[xi]
    if pos == n-1:
        lpos = pos-1
        lnum = pos2num[lpos]
        num2pos[xi] = lpos
        num2pos[lnum] = pos
        pos2num[pos] = lnum
        pos2num[lpos] = xi

    else:
        rpos = pos+1
        rnum = pos2num[rpos]
        num2pos[xi] = rpos
        num2pos[rnum] = pos
        pos2num[pos] = rnum
        pos2num[rpos] = xi

for i in range(n):
    pos2num[i] += 1

print(*pos2num)
