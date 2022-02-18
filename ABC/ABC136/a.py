a, b, c = map(int, input().split())

a = min(b + c, a)
c = b + c - a

print(c)