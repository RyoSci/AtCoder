n = int(input())

res = 0
for i in range(10 ** 4):
    res += i
    if res >= n:
        break

rest = res - n
for i in range(1, i + 1):
    if rest > 0:
        i -= 1
        rest -= 1
    if i != 0:
        print(i)
