a, b = map(int, input().split())

res = b // 4 - (a - 1) // 4 - (b // 100 - (a - 1) // 100) + \
    b // 400 - (a - 1) // 400
print(res)
