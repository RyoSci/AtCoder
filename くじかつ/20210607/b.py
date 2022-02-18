a, b, c = sorted(list(map(int, input().split())))
res = 0
if a % 2 == b % 2:
    res += (b-a)//2
else:
    c += 1
    b += 1
    res += (b-a)//2+1
res += (c-b)
print(res)
