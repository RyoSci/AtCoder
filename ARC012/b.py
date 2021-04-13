n, va, vb, l = map(int, input().split())

for i in range(n):
    time = l / va
    l = vb * time

print(l)