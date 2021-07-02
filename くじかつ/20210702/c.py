n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    if a[a[i]-1] == i+1:
        res += 1

print(res//2)
