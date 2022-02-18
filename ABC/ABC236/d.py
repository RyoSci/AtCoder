import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = []

for i in range(2*n-1):
    ai = list(map(int, input().split()))
    ai = [0]*(2*n-len(ai)) + ai
    a.append(ai)


# n = 8
# a = [[10**9]*(2*n) for _ in range(2*n-1)]

seen = [0]*2*n

ans = 0


def f(array):
    res = array[0]
    for i in array[1:]:
        res ^= i
    return res


def dfs(i, array):
    global ans
    if i == 2*n:
        ans = max(ans, f(array))
        return
    if seen[i] == 1:
        dfs(i+1, array)
    else:
        for chi in range(i+1, 2*n):
            if seen[chi] == 1:
                continue
            seen[chi] = 1
            dfs(i+1, array+[a[i][chi]])
            seen[chi] = 0


dfs(0, [])
print(ans)
