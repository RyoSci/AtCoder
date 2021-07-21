n = int(input())
j, b = 0, 0

for i in range(n):
    u, x = input().split()
    if x == "JPY":
        u = int(u)
        j += u
    else:
        u = float(u)
        b += u

print(j+b*380000.0)
