import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

h = q-p+1
w = s-r+1

ans = [["."]*(w) for _ in range(h)]


def f(k):
    if max(1-a, 1-b) <= k <= min(n-a, n-b):
        return True
    return False


def g(k):
    if max(1-a, b-n) <= k <= min(n-a, b-1):
        return True
    return False


for i in range(p, p+h):
    for j in range(r, r+w):
        kx = i-a
        ky = j-b
        ky2 = b-j
        if kx == ky:
            if f(kx):
                if f(ky):
                    ans[i-p][j-r] = "#"
                # if g(ky2):
                #     ans[i-p][j-r] = "#"
        if kx == ky2:
            if g(kx):
                # if f(ky):
                #     ans[i-p][j-r] = "#"
                if g(ky2):
                    ans[i-p][j-r] = "#"

for i in range(h):
    print(*ans[i], sep="")
