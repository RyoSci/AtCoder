import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
# n = 2*10**5
# a = [2*10**5]*n

p = [-1]*(2*10**5+1)


def find(x):
    if p[x] == -1:
        return x
    p[x] = find(p[x])
    return p[x]


def unite(a, b):
    if find(a) == find(b):
        return
    p[find(a)] = find(b)
    return


ans = 0
for i in range(n//2):
    if find(a[i]) == find(a[-i-1]):
        continue
    else:
        unite(a[i], a[-i-1])
        ans += 1

print(ans)
