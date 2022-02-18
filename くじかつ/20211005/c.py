import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range((1 << n)-1):
    tmp = 1
    for j in range(n):
        if i >> j & 1:
            if a[j] % 2 == 0:
                tmp *= 2
        else:
            if a[j] % 2 == 1:
                tmp *= 2
    res += tmp

print(res)
