from bisect import bisect_left
h, w, n = map(int, input().split())
a = []
b = []
a_s = set()
b_s = set()
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    a_s.add(ai)
    b_s.add(bi)

a_s = sorted(list(a_s))
b_s = sorted(list(b_s))

for i in range(n):
    ai = bisect_left(a_s, a[i])
    bi = bisect_left(b_s, b[i])
    print(ai+1, bi+1)
