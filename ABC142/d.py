a, b = map(int, input().split())
# a = 10**9+7
# b = a * 2
# a = a * 3
div = dict()
div[1] = 1
for i in range(2, 10 ** 6 + 1):
    while a % i == 0 and b % i == 0:
        a //= i
        b //= i
        div[i] = 1

while 1:
    c = a % b
    a = b
    b = c
    if b == 0:
        div[a] = 1
        break

print(len(div))
