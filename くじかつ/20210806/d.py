n = int(input())


def f(x):
    return (1+x)*x//2


res = 0
for i in range(1, n+1):
    res += i*f(n//i)

print(res)
