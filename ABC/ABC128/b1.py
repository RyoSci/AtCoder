n  = int(input())

city_points = []
for i in range(n):
    s, p = input().split()
    city_points.append([s, -int(p), i + 1])

city_points.sort()

for i in city_points:
    print(i[-1])