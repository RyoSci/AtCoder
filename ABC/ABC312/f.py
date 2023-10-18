# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, m = map(int, input().split())

t = [[] for _ in range(3)]
t1id = []
tx = []
for i in range(n):
    ti, xi = map(int, input().split())
    t[ti].append(xi)

    tx.append((ti, xi))
    if ti == 1:
        t1id.append(i)

for i in range(3):
    t[i].sort(reverse=True)

t0_cnt = len(t[0])
t0_cnt = min(m, t0_cnt)

now = sum(t[0][:t0_cnt])
rest = m-t0_cnt
ans = now

t[0] = t[0][:t0_cnt]
t[1].sort()
t[2].sort()


while len(t[2]):

    if rest <= 0 and len(t[0]) == 0:
        break

    rest -= 1
    t2use = t[2].pop()

    for i in range(t2use):
        if len(t[1]) == 0:
            break

        if rest > 0:
            top = t[1].pop()
            now += top
            rest -= 1
        elif rest == 0:
            if len(t[0]) > 0:
                bottom = t[0].pop()
                now -= bottom

                top = t[1].pop()
                now += top
            else:
                break
        else:
            if len(t[0]) > 1:
                bottom = t[0].pop()
                now -= bottom
                bottom = t[0].pop()
                now -= bottom

                top = t[1].pop()
                now += top
                rest += 1
            else:
                break

        ans = max(ans, now)


print(ans)
