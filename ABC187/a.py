a, b = input().split()


def s(x):
    return int(x[0]) + int(x[1]) + int(x[2])


if s(a) >= s(b):
    print(s(a))
else:
    print(s(b))
