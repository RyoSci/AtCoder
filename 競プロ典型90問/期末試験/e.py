p, q, r, k = map(int, input().split())
p_, q_, r_ = p, q, r
memo = [[[-1 for i in range(10)] for j in range(10)] for k in range(10)]


flag = False
for i in range(4, k+1):
    r, q, p = r % 10, q % 10, p % 10
    if memo[p][q][r] == -1:
        memo[p][q][r] = i
    else:
        start = memo[p][q][r]
        end = i
        cycle = end-start
        flag = True
        break
    a = p+q+r
    a %= 10
    r, q, p = a, r, q

if flag:
    if k-start >= cycle:
        k = start+(k-start) % cycle

p, q, r = p_, q_, r_
for i in range(4, k+1):
    a = p+q+r
    a %= 10
    r, q, p = a, r, q

print(a)
