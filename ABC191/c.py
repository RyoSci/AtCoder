h, w = map(int, input().split())
s = [input() for _ in range(h)]

edge_num = 0
for i in range(1, h):
    length = 0
    for j in range(w):
        if s[i][j] != s[i-1][j]:
            length += 1
        else:
            if length:
                edge_num += 1
                length = 0

for j in range(1, w):
    length = 0
    for i in range(h):
        if s[i][j] != s[i][j-1]:
            length += 1
        else:
            if length:
                edge_num += 1
                length = 0

print(edge_num)
