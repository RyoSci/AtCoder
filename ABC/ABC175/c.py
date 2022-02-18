x, k, d = map(int, input().split())
x = abs(x)
mod = x % d
max_move = x - k * d

if mod < max_move:
    res = max_move
else:
    rest = k - x // d
    if rest % 2 == 0:
        res = mod
    else:
        res = abs(mod - d)

print(res)