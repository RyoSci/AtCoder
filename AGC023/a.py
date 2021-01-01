n = int(input())
a = [0] + list(map(int, input().split()))
same_points = dict()
same_points[0] = 1
for i in range(n):
    a[i + 1] += a[i]
    if a[i + 1] not in same_points:
        same_points[a[i + 1]] = 1
    else:
        same_points[a[i + 1]] += 1

ans = 0
for val in same_points.values():
    ans += val * (val - 1) // 2

print(ans)
