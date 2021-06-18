n = int(input())
a = [0]+list(map(int, input().split()))+[0]
total = 0

for i in range(n+1):
    total += abs(a[i+1]-a[i])

for j in range(n):
    res = total-abs(a[j+1]-a[j]) - abs(a[j+2]-a[j+1])+abs(a[j+2]-a[j])
    print(res)
