# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = [input() for _ in range(9)]
ans = 0
for si in range(9):
    for sj in range(9):
        if s[si][sj] == ".":
            continue
        for ti in range(9):
            for tj in range(9):
                if s[ti][tj] == ".":
                    continue
                if (si, sj) == (ti, tj):
                    continue
                di = ti-si
                dj = tj-sj

                ni = -dj
                nj = di
                if 0 <= ni+si < 9 and 0 <= nj+sj < 9 and s[si+ni][sj+nj] == '#':
                    if 0 <= ni+ti < 9 and 0 <= nj+tj < 9 and s[ti+ni][tj+nj] == '#':
                        ans += 1
                        # print(si, sj, ti, tj, ni+si, nj+sj,
                        #       ni+ti, nj+tj, ni, nj, "AAA")

                ni = dj
                nj = -di
                if 0 <= ni+si < 9 and 0 <= nj+sj < 9 and s[si+ni][sj+nj] == '#':
                    if 0 <= ni+ti < 9 and 0 <= nj+tj < 9 and s[ti+ni][tj+nj] == '#':
                        ans += 1
                        # print(si, sj, ti, tj, ni+si, nj +
                        #       sj, ni+ti, nj+tj, ni, nj)


print(ans//4//2)
