n, m = map(int, input().split())
node = [0] * n
for i in range(m):
    u, v, c = map(int, input().split())
    if node[u - 1] == 0 and node[v - 1] == 0:
        node[u - 1] = c
        if c == n:
            node[v - 1] = c - 1
        else:
            node[v - 1] = c + 1
    elif node[u - 1] == 0 and node[v - 1] != 0:
        if node[v - 1] == c:
            if c == n:
                node[v - 1] = c - 1
            else:
                node[u - 1] = c + 1
        else:
            node[u - 1] = c
    elif node[u - 1] != 0 and node[v - 1] == 0:
        if node[u - 1] == c:
            if c == n:
                node[v - 1] = c - 1
            else:
                node[v - 1] = c + 1
        else:
            node[v - 1] = c
    else:
        if node[u - 1] == node[v - 1] == c:
            if c == 1:
                node[u - 1] += 1
            else:
                node[u - 1] -= 1

if 0 in node:
    print("No")
else:
    for i in range(n):
        print(node[i])
