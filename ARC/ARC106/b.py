import sys
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = [i for i in range(n)]


class UnionFind:
    global p

    def find(self, x):
        if p[x] == x:
            return x
        else:
            p[x] = self.find(p[x])
            return p[x]

    def union(self, x, y):
        if self.find(x) == self.find(y):
            return
        else:
            p[self.find(x)] = self.find(y)
            return


uf = UnionFind()
for i in range(m):
    c, d = map(lambda x: int(x) - 1, input().split())
    uf.union(c, d)

group = {}
for i in range(n):
    pi = p[i]
    if uf.find(pi) not in group:
        group[uf.find(pi)] = [i]
    else:
        group[uf.find(pi)].append(i)

ans = "Yes"
for key, vals in group.items():
    a_sum, b_sum = 0, 0
    for val in vals:
        a_sum += a[val]
        b_sum += b[val]
    if a_sum != b_sum:
        ans = "No"
        break
print(ans)
