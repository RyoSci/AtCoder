n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_mod = [0]*46
b_mod = [0]*46
c_mod = [0]*46

for i in range(n):
    a_mod[a[i] % 46] += 1
    b_mod[b[i] % 46] += 1
    c_mod[c[i] % 46] += 1

res = 0
for i in range(46):
    for j in range(46):
        res += a_mod[i]*b_mod[j]*c_mod[(-i-j) % 46]

print(res)
