import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
min_cnt = 0
min_abs = 10**18
total = 0
for i in range(n):
    if a[i] < 0:
        min_cnt += 1
    min_abs = min(min_abs, abs(a[i]))
    total += abs(a[i])

if min_cnt % 2 == 0:
    print(total)
else:
    print(total-2*min_abs)
