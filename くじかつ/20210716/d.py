n, x = map(int, input().split())

pnum = [0]*(n+1)
pnum[0] = 1
total = [0]*(n+1)
total[0] = 1

for i in range(n):
    pnum[i+1] = pnum[i]*2+1
    total[i+1] = total[i]*2+3


def dfs(i, x, cnt):
    if i == 0:
        return cnt+1
    mid = 2+total[i-1]
    if x == 1:
        return cnt
    elif x == mid:
        return cnt+pnum[i-1]+1
    elif x == 3+total[i-1]*2:
        return cnt+pnum[i-1]*2+1
    elif x < mid:
        return dfs(i-1, x-1, cnt)
    else:
        return dfs(i-1, x-mid, cnt+pnum[i-1]+1)


res = dfs(n, x, 0)
print(res)
