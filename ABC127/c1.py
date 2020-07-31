n, m = map(int, input().split())
l_max = 1
r_min = 10 ** 5
for i in range(m):
    l, r = map(int, input().split())
    l_max = max(l, l_max)
    r_min = min(r, r_min)

print(max(0, r_min - l_max + 1))



