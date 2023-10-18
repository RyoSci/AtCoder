# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = []
for i in range(n):
    si = input()
    s.append(list(si))


b = []
for i in range(m):
    b.append([a[i], i])

b.sort(reverse=True)

for i in range(n):
    now = i + 1
    for j in range(m):
        if s[i][j] == "o":
            now += a[j]

    others = [0]*n
    for j in range(n):
        if i == j:
            continue
        others[j] += j+1
        for k in range(m):
            if s[j][k] == "o":
                others[j] += a[k]

    max_others = max(others)
    cnt = 0
    for j in range(m):
        if now > max_others:
            break

        if s[i][b[j][-1]] == "x":
            cnt += 1
            now += a[b[j][-1]]

    print(cnt)
