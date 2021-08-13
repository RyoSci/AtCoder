n = int(input())


def f(x):
    if x < 10:
        return x
    return f(x//10)+x % 10


if n % f(n) == 0:
    print("Yes")
else:
    print("No")
