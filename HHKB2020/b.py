h, w = map(int, input().split())
s = [input() for i in range(h)]

counter = 0
for i in range(h):
    for j in range(w - 1):
        if s[i][j] == "." and s[i][j + 1] == ".":
            counter += 1


for j in range(w):
    for i in range(h - 1):
        if s[i][j] == "." and s[i + 1][j] == ".":
            counter += 1

print(counter)
