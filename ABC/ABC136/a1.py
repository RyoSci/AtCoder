a, b, c =map(int, input().split())
move = min(a - b, c)

b += move
c -= move

print(c)