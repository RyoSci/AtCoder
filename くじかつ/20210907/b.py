import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n-1):
    ti, li, ri = a[i]
    if ti == 2:
        ri -= 0.0000001
    elif ti == 3:
        li += 0.0000001
    elif ti == 4:
        ri -= 0.0000001
        li += 0.0000001

    for j in range(i+1, n):
        tj, lj, rj = a[j]
        if tj == 2:
            rj -= 0.0000001
        elif tj == 3:
            lj += 0.0000001
        elif tj == 4:
            rj -= 0.0000001
            lj += 0.0000001
        if not(rj < li or ri < lj):
            res += 1
print(res)
