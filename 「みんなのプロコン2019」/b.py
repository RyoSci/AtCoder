road = dict()

for i in range(3):
    a, b = map(int, input().split())
    if not a in road:
        road[a] = 1
    else:
        road[a] += 1
    if not b in road:
        road[b] = 1
    else:
        road[b] += 1

ans = "NO"
if len(road) == 4 and max(road.values()) <= 2:
    ans = "YES"

print(ans)
