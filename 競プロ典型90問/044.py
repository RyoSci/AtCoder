n, q = map(int, input().split())
a = list(map(int, input().split()))
swift = 0

for i in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        a[(x-swift) % n], a[(y-swift) % n] = a[(y-swift) % n], a[(x-swift) % n]
    elif t == 2:
        swift += 1
    else:
        print(a[(x-swift) % n])
