# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
c = []
for i in range(h):
    ci = list(input())
    c.append(ci)

n = min(h, w)
ans = [set() for _ in range(n+1)]
for i in range(h):
    for j in range(w):
        if c[i][j] == ".":
            continue

        cnt = 1
        ni = i-1
        nj = j+1
        while 0 <= ni < h and 0 <= nj < w:
            if c[ni][nj] == "#":
                cnt += 1
                ni -= 1
                nj += 1
            else:
                break
        ni += 1
        nj -= 1

        pi = i+1
        pj = j-1
        while 0 <= pi < h and 0 <= pj < w:
            if c[pi][pj] == "#":
                cnt += 1
                pi += 1
                pj -= 1
            else:
                break
        pi -= 1
        pj += 1

        ci = (ni+pi)//2
        cj = (nj+pj)//2

        cnt //= 2
        ans[cnt].add((ci, cj))

for i in range(1, n+1):
    print(len(ans[i]))
