import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

m = set()


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dx = xy[j][0]-xy[i][0]
        dy = xy[j][1]-xy[i][1]

        if dx == 0:
            if dy > 0:
                m.add((0, 1))
            else:
                m.add((0, -1))
        elif dy == 0:
            if dx > 0:
                m.add((1, 0))
            else:
                m.add((-1, 0))
        else:
            num = gcd(abs(dx), abs(dy))
            m.add((dx//num, dy//num))

print(len(m))
