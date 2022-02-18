k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(a[0]+k)

dis = 0
for i in range(n):
    dis = max(dis, a[i+1]-a[i])

print(k-dis)
