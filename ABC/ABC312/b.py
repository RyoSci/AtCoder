# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
s = []

for i in range(n):
    si = input()
    s.append(si)

for i in range(n):
    for j in range(m):

        flag = True
        for ii in range(9):
            for jj in range(9):

                ni = i+ii
                nj = j+jj
                if not (ni < n and nj < m):
                    flag = False
                    break

                if ii < 3 and jj < 3:
                    if s[ni][nj] == ".":
                        flag = False
                        break
                elif ii == 3 and jj <= 3:
                    if s[ni][nj] == "#":
                        flag = False
                        break
                elif jj == 3 and ii <= 3:
                    if s[ni][nj] == "#":
                        flag = False
                        break

                elif ii > 5 and jj > 5:
                    if s[ni][nj] == ".":
                        flag = False
                        break
                elif ii == 5 and jj >= 5:
                    if s[ni][nj] == "#":
                        flag = False
                        break
                elif jj == 5 and ii >= 5:
                    if s[ni][nj] == "#":
                        flag = False
                        break

            if not flag:
                break

        if flag:
            print(i+1, j+1)
