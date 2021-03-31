n, l = map(int, input().split())
amdkj = [input() for _ in range(l)]
leader = input()
x = l - 1
y = leader.index("o")

while x >= 0:
    for i in [-1, 1]:
        if 0 <= y + i < 2 * n - 2:
            if amdkj[x][y + i] == "-":
                x -= 1
                y += 2 * i
                break
    else:
        x -= 1

print(y // 2 + 1)
