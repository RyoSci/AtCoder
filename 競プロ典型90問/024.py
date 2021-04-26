n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dis = 0
for i in range(n):
    dis += abs(a[i] - b[i])

if dis > k:
    ans = "No"
elif (k - dis) % 2 == 1:
    ans = "No"
else:
    ans = "Yes"
print(ans)
