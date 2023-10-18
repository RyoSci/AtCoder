

def check(g):
    for i in range(2):
        if g[i][0] >= g[i][1]:
            return False
    for i in range(2):
        if g[0][i] >= g[1][i]:
            return False
    return True


def rotate(g):
    g = list(zip(*g[::-1]))
    return g


t = int(input())
for _ in range(t):
    g = []
    for i in range(2):
        gi = list(map(int, input().split()))
        g.append(gi)

    ans = False
    for i in range(4):
        g = rotate(g)
        if check(g):
            ans = True

    if ans:
        print("YES")
    else:
        print("NO")
