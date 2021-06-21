n, m = map(int, input().split())
s = input()
t = input()

# n, m = 10**5-1, 10**5
# s = "a"*n
# t = "b"*m


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


l = n*m//gcd(n, m)


x = dict()

for i in range(n):
    x[i*l//n] = s[i]

for j in range(m):
    if j*l//m not in x:
        continue
    elif x[j*l//m] == t[j]:
        continue
    else:
        print(-1)
        exit()
else:
    print(l)
