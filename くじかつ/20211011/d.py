import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x = map(int, input().split())

bpb = [[0]*3 for _ in range(n+1)]
bpb[1] = [1, 3, 5]
for i in range(2, n+1):
    bpb[i][0] = bpb[i-1][0]
    bpb[i][1] = bpb[i-1][1]*2+1
    bpb[i][2] = bpb[i-1][2]*2+3


def f(x, i, cnt):
    if i == 1:
        if x == 1:
            return cnt+0
        elif x == 2:
            return cnt+1
        if x == 3:
            return cnt+2
        if x == 4:
            return cnt+3
        if x == 5:
            return cnt+3
    if x == bpb[i][0]:
        return cnt
    elif bpb[i][0] < x < bpb[i][1]:
        return f(x-1, i-1, cnt)
    elif x == bpb[i][1]:
        return cnt+bpb[i-1][1]+1
    elif bpb[i][1] < x < bpb[i][2]:
        return f(x-bpb[i][1], i-1, cnt+bpb[i-1][1]+1)
    elif x == bpb[i][2]:
        return cnt+bpb[i-1][1]*2+1


print(f(x, n, 0))
