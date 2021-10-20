import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b, w = map(int, input().split())
w *= 1000
res = []
for i in range(1, 10**7):
    if i*a <= w <= i*b:
        res.append(i)

if len(res) == 0:
    print("UNSATISFIABLE")
else:
    print(res[0], res[-1])
