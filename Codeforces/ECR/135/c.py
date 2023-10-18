# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = []
    heapify(q)
    da = dict()
    db = dict()
    seen_a = [0]*n
    seen_b = [0]*n

    for i in range(n):
        if a[i] not in da:
            da[a[i]] = []
        da[a[i]].append(i)
        heappush(q, (-a[i], 1, i))

    for i in range(n):
        if b[i] not in db:
            db[b[i]] = []
        db[b[i]].append(i)
        heappush(q, (-b[i], 0, i))
        # if b[i] in da:
        #     while len(da[b[i]]) > 0:
        #         j = da[num].pop()
        #         if seen_a[j] == 0:
        #             seen_a[j] = 1
        #             seen_b[i] = 1
        #             break
        #     if seen_b[i] == 0:
        #         if b[i] not in db:
        #             db[b[i]] = []
        #         db[b[i]].append(i)
        #         heappush((-b[i], 1, i))

        # else:
        #     if b[i] not in db:
        #         db[b[i]] = []
        #     db[b[i]].append(i)
        #     heappush((-b[i], 1, i))

    ans = 0
    while len(q) > 0:
        num, is_a, i = heappop(q)
        num = -num
        if is_a:
            if seen_a[i] == 1:
                continue
            if num in db:
                while len(db[num]) > 0:
                    j = db[num].pop()
                    if seen_b[j] == 0:
                        seen_b[j] = 1
                        seen_a[i] = 1
                        break
            if seen_a[i] == 0:
                num = len(str(num))
                if num not in da:
                    da[num] = []
                da[num].append(i)
                heappush(q, (-num, is_a, i))
                ans += 1

        else:
            if seen_b[i] == 1:
                continue
            if num in da:
                while len(da[num]) > 0:
                    j = da[num].pop()
                    if seen_a[j] == 0:
                        seen_a[j] = 1
                        seen_b[i] = 1
                        break
            if seen_b[i] == 0:
                num = len(str(num))
                if num not in db:
                    db[num] = []
                db[num].append(i)
                heappush(q, (-num, is_a, i))

                ans += 1

    print(ans)
