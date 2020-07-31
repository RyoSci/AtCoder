n = int(input())
city_to_points = dict()

for i in range(n):
    s, p = input().split()
    p = int(p)
    if s not in city_to_points:
        city_to_points[s] = [[p, i + 1]]
    else:
        city_to_points[s].append([p, i + 1])

kyes = list(city_to_points.keys())
kyes.sort()

for i in kyes:
    restrans = city_to_points[i]
    restrans.sort(reverse=True)
    for j in restrans:
        print(j[1])