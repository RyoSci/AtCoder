import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0]*(10**5+1)

for i in a:
    d[i] += 1

res = 0
for i in range(10**5):
    tmp = 0
    if i-1 >= 0:
        tmp += d[i-1]
    if i+1 <= 10**5:
        tmp += d[i+1]
    tmp += d[i]
    res = max(res, tmp)

print(res)
