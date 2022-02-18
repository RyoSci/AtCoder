a, b= map(int, input().split())

res = 0
if a >= 13:
    res = b
elif a >= 6:
    res = b // 2
else:
    res = 0

print(res)
