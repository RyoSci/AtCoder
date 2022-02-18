x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

pi = 0
ri = 0
ans = 0
for i in range(x):
    if ri < c and p[pi] < r[ri]:
        ans += r[ri]
        ri += 1
    else:
        ans += p[pi]
        pi += 1

tmp = r[:ri]
r[:ri] = p[pi:pi + ri]
p[pi:pi + ri] = tmp

q = q + r
q.sort(reverse=True)
for i in range(y):
    ans += q[i]

print(ans)
print(p)
print(q)
print(r)
