n, t = map(int, input().split())
open = [0] * (10 ** 6 + 2 + t)
for i in range(n):
    a = int(input())
    open[a] += 1
    open[a + t] -= 1

timer = 0
for i in range(1, len(open)):
    open[i] += open[i - 1]
    if open[i] >= 1:
        timer += 1
print(timer)
