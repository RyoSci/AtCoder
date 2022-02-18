import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
flag = 0
cnt = 1
for i in range(n-1):
    if a[i] > a[i+1]:
        now = 1
    elif a[i] == a[i+1]:
        now = 0
    else:
        now = -1
    if flag == 0:
        flag = now
        continue
    elif flag == 1:
        if now == -1:
            cnt += 1
            flag = 0
    else:
        if now == 1:
            cnt += 1
            flag = 0

print(cnt)
