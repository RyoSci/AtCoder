n = int(input())

res = 0
for i in range(1, 10**5):
    if i*i <= n:
        res = i*i

print(res)
