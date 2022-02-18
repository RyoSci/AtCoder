a, b = map(int, input().split())
b -= 1
a = (b + (a - 2)) // (a - 1)
print(a)