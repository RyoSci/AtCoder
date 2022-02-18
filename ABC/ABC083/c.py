x, y = map(int, input().split())
tmp_memo = 1
for l in range(2, 100):
    tmp_memo *= 2
    if tmp_memo * x > y:
        l -= 1
        break

print(l)
