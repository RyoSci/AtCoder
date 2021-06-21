n = int(input())
a = list(map(int, input().split()))

mod = [0]*200
for i in range(n):
    mod[a[i] % 200] += 1

res = 0
for i in range(200):
    res += mod[i]*(mod[i]-1)//2

print(res)
