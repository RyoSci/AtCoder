n = int(input())
x = list(map(int, input().split()))
m = 0
u = 0
c = 0
for i in range(n):
    tmp = abs(x[i])
    m += tmp
    u += tmp ** 2
    c = max(c, tmp)

print(m)
print(u ** 0.5)
print(c)
