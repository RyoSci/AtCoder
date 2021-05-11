n = int(input())


def euclid(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    else:
        return True


res = 0
for i in range(2, n):
    res += euclid(i)

print(res)
