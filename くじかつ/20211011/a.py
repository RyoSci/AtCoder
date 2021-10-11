import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for x in range(1, 1001):
    for i in range(n):
        if a[i] <= x <= b[i]:
            continue
        else:
            break
    else:
        res += 1

print(res)
