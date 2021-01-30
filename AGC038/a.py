h, w, a, b = map(int, input().split())
s = "0" * a + "1" * (w - a)
t = "1" * a + "0" * (w - a)

for i in range(h):
    if i >= b:
        print(t)
    else:
        print(s)
