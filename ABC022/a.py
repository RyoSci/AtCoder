n, s, t = map(int, input().split())
w = int(input())
res = 0
for i in range(n):
    if i == 0:
        pass
    else:
        w += int(input())
    if s <= w <= t:
        res += 1
print(res)
