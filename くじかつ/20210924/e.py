import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
water = set()
sugar = set()

for i in range(0, f+1, a):
    for j in range(0, f+1, b):
        if 100*i+100*j <= f:
            water.add(100*i+100*j)

for i in range(0, f+1, c):
    for j in range(0, f+1, d):
        if i+j <= f:
            sugar.add(i+j)

water.remove(0)
sugar.remove(0)

res_w = 100*a
res_s = 0
for i in water:
    for j in sugar:
        if j*(100+e) <= e*(i+j) and i+j <= f:
            if (i+j)*res_s < j*(res_w+res_s):
                res_w = i
                res_s = j

print(res_w+res_s, res_s)
