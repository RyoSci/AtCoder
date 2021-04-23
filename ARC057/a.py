a, k = map(int, input().split())

goal = 2 * 10 ** 12
if k == 0:
    res = goal - a
else:
    def f(t, res):
        if t >= goal:
            return res
        return f(t * (1 + k) + 1, res + 1)
    res = f(a, 0)

print(res)
