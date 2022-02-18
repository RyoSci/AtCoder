n = int(input())
min_dis = 10 ** 10
max_dis = 0
for i in range(n):
    x, y = map(int, input().split())
    tmp1 = x + y
    min_dis = min(tmp1, min_dis)
    max_dis = max(tmp1, max_dis)

print(abs(max_dis - min_dis))
