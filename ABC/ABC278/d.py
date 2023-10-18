# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
q = int(input())

stage = -1
chage = dict()

ans = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        stage = x
        chage.clear()

    elif query[0] == 2:
        i, x = query[1:]
        i -= 1
        if stage == -1:
            a[i] += x
        else:
            if i not in chage:
                chage[i] = stage
            chage[i] += x

    else:
        i = query[1]
        i -= 1
        if stage == -1:
            ans.append(a[i])
        else:
            if i not in chage:
                ans.append(stage)
            else:
                ans.append(chage[i])


print(*ans)
