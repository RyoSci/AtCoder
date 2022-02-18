from typing import Coroutine


n = int(input())
st = [list(input().split()) for _ in range(n)]
x = input()

flag = False
res = 0
for s, t in st:
    if s == x:
        flag = True
        continue
    if flag:
        res += int(t)

print(res)
