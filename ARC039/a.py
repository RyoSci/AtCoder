a, b = map(int, input().split())

res = -1000
for i in range(3):
    for j in range(10):
        if i == 0 and j == 0:
            continue
        a_ = a - int(str(a)[i]) * 10 ** (2 - i)
        a_ += j * 10 ** (2 - i)
        res = max(res, a_ - b)
        
for i in range(3):
    for j in range(10):
        if i == 0 and j == 0:
            continue
        b_ = b - int(str(b)[i]) * 10 ** (2 - i)
        b_ += j * 10 ** (2 - i)
        res = max(res, a - b_)
        
print(res)