n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt_b = [0]*n
for i in range(n):
    cnt_b[c[i]-1] += 1

cnt_a = [0]*10**5
for i in range(n):
    cnt_a[a[i]-1] += 1

res = 0
for i in range(n):
    res += cnt_b[i]*cnt_a[b[i]-1]

print(res)
