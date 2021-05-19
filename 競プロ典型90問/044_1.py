from queue import deque
n, q = map(int, input().split())
a = list(map(int, input().split()))
d = deque(a)

for i in range(q):
    t, x, y = map(lambda x: int(x)-1, input().split())
    if t == 0:
        d[x], d[y] = d[y], d[x]
    elif t == 1:
        d.appendleft(d.pop())
    else:
        print(d[x])
