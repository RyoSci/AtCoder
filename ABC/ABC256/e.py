# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
n = int(input())
x = list(map(lambda x: int(x)-1, input().split()))
c = list(map(int, input().split()))


seen = [0]*n
finished = [0]*n
ans = 0


def dfs(i):
    global ans
    seen[i] = 1
    ni = x[i]
    if finished[ni]:
        pass
    elif seen[ni] and not finished[ni]:
        tmp = [c[ni]]
        nni = x[ni]
        while nni != ni:
            tmp.append(c[nni])
            nni = x[nni]
        ans += min(tmp)
    else:
        dfs(ni)
    finished[i] = 1
    return


for i in range(n):
    if seen[i]:
        continue
    dfs(i)

print(ans)
