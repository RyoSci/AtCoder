k = int(input())

d = dict()


def add(x):
    if x not in d:
        d[x] = 0
    d[x] += 1


for i in range(2, 10**6+1):
    while k % i == 0:
        add(i)
        k //= i
if k != 1:
    add(k)


def cal(x):
    tmp = 1
    for i in range(x+2, x, -1):
        tmp *= i
    return tmp//2


total = 1
for val in d.values():
    total *= cal(val)

flag = True
for val in d.values():
    if val % 3 != 0:
        flag = False
        break

rest = 0
if flag:
    total -= 1
    rest += 1

tmp = 1
for val in d.values():
    tmp *= val//2+1

if flag:
    tmp -= 1

total -= tmp*3
rest += tmp


print(total//6+rest)
