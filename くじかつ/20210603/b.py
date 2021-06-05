n = int(input())
l = list(map(int, input().split()))

res = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            max_ = max(l[i], l[j], l[k])
            if l[i]+l[j]+l[k]-max_ > max_ and l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                res += 1

print(res)
