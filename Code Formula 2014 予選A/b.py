a, b, = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
pin = ["x"] * 10

for i in range(a):
    pin[p[i]-1] = "."
for i in range(b):
    pin[q[i]-1] = "o"

res = []
now = 0
for i in range(1, 5):
    tmp = " "*(4-i)
    for j in range(i):
        tmp += str(pin[now])
        tmp += " "
        now += 1
    res.append(tmp)

for i in res[::-1]:
    print(i)
