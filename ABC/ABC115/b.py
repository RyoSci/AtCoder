n = int(input())
p = [0] * n

for i in range(n):
    p[i] = int(input())

p.sort(reverse=True)
 
res = p[0] // 2 + sum(p[1:])

print(res)