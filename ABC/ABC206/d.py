n = int(input())
a = list(map(int, input().split()))


par = [i for i in range(2*10**5+1)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])  # 経路圧縮
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


cnt = 0
for i in range(n//2):
    if same(a[i], a[-i-1]):
        continue
    else:
        unite(a[i], a[-i-1])
        cnt += 1
print(cnt)
