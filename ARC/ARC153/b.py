# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
g = []
for i in range(h):
    s = input()
    g.append(list(s))

q = int(input())
h_now = 0
w_now = 0


def f(hw: int, now: int, aibi: int) -> int:
    if 0 <= now <= aibi:
        now = abs(aibi-now)
    else:
        now = hw - abs(now-aibi)

    return now


for i in range(q):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1

    h_now = f(h, h_now, ai)
    w_now = f(w, w_now, bi)

    # print(h_now, w_now)

hs = [-1]*h
ws = [-1]*w


def g(hws: list, hw: int, now: int) -> int:
    for i in range(hw):
        hws[now] = i
        if q % 2 == 0:
            now += 1
        else:
            now -= 1

        now %= hw


g(hs, h, h_now)
g(ws, w, w_now)

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(g[hs[i]][ws[j]])
    print("".join(ans))
