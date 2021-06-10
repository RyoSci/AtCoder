n, m = map(int, input().split())
odd = 0
even = 0

for i in range(n):
    s = input()
    tmp = 0
    for j in s:
        if j == "1":
            tmp += 1
    if tmp % 2 == 1:
        odd += 1
    else:
        even += 1


def f(x):
    return x*(x-1)//2


print(f(n)-f(odd)-f(even))
