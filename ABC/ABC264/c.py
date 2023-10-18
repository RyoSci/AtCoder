# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys

from numpy import append
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h1, w1 = map(int, input().split())
a = []
for i in range(h1):
    ai = list(map(int, input().split()))
    a.append(ai)

h2, w2 = map(int, input().split())
b = []
for i in range(h2):
    bi = list(map(int, input().split()))
    b.append(bi)


ans = "No"
for i in range(1 << h1):
    tmp = []
    for j in range(h1):
        if i >> j & 1:
            tmp.append(a[j])

    if len(tmp) != len(b):
        continue

    for j in range(1 << w1):
        tmp1 = [[] for _ in range(h2)]
        for k in range(w1):
            if j >> k & 1:
                for l in range(h2):
                    tmp1[l].append(tmp[l][k])

        if b == tmp1:
            ans = "Yes"
            print(ans)
            exit()
    # res = 0
    # for j in range(h2):
    #     now = 0
    #     cnt = 0
    #     for k in range(w2):
    #         while now < w1:
    #             if b[j][k] == tmp[j][now]:
    #                 cnt += 1
    #                 now += 1
    #                 break
    #             else:
    #                 now += 1

    #     if cnt == w2:
    #         res += 1
    # if res == h2:
    #     ans = "Yes"

print(ans)
