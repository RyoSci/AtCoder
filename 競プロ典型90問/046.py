n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_map = [0]*46
b_map = [0]*46
c_map = [0]*46

for x, x_map in zip([a, b, c], [a_map, b_map, c_map]):
    for i in range(n):
        x_map[x[i] % 46] += 1


res = 0
for ai in range(46):
    for bi in range(46):
        for ci in range(46):
            if (ai+bi+ci) % 46 == 0:
                res += a_map[ai]*b_map[bi]*c_map[ci]

print(res)
