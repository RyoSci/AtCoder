n, p = map(int, input().split())
a = list(map(int, input().split()))
mods = [0] * 2
for i in range(n):
    if a[i] % 2 == 0:
        mods[0] += 1
    else:
        mods[1] += 1

factrial = [1] * (max(mods) + 1)
for i in range(1, (max(mods) + 1)):
    factrial[i] *= factrial[i - 1] * i

res = 0
for i in range(mods[1] + 1):
    if i % 2 == p:
        res += factrial[mods[1]] // (factrial[i] * factrial[mods[1] - i])
res *= 2 ** (mods[0])
print(res)
