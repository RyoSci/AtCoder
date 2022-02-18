n, q = map(int, input().split())
a = [0]+list(map(int, input().split()))+[10**19]

query = []
for i in range(q):
    query.append([int(input()), i])
