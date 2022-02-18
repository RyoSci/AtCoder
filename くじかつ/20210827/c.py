n = int(input())
a = list(map(int, input().split()))

x = 2*n
y = 2*sum(a)

l = y//x
r = (y+x-1)//x

tmpl = 0
tmpr = 0
for i in range(n):
    tmpl += (l-a[i])**2
    tmpr += (r-a[i])**2

print(min(tmpl, tmpr))
