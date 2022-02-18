from math import factorial as f
s = int(input())
div = s // 3
mod = s % 3
a = 10 ** 9 + 7
res = 0
while div != 0:
    res = (res + f(div - 1 + mod) // (f(div - 1) * f(mod))) % a
    div -= 1
    mod += 3

print(res)
