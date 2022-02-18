n, k = map(int, input().split())
a = list(map(int, input().split()))

now = k
res = 1
while now < n:
    now += k-1
    res += 1

print(res)
