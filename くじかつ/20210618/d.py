n = int(input())

for i in range(int(n**0.5)+1, 0, -1):
    if n % i == 0:
        a = i
        break

b = n//a


def f(a, b):
    return max(len(str(a)), len(str(b)))


print(f(a, b))
