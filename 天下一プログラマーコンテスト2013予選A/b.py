n = int(input())
res = 0
for i in range(n):
    if 0 <= sum(map(int, input().split())) < 20:
        res += 1

print(res)
