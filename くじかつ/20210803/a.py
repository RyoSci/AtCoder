n = int(input())
res = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        pass
    else:
        res += i

print(res)
