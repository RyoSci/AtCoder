import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w, k = list(map(int, input().split()))
s = [list(input().strip()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        s[i][j] = int(s[i[j]])

for i in range(1 << (h-1)):
    h_split = []
    for j in range(h-1):
        if i >> j & 1:
            h_split.append(j)
    m = len(h_split)
    memo = [[0]*m for _ in range(w)]
    memo[i][j] < -i番目のグループのj列目の個数
