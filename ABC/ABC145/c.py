import itertools

n = int(input())
town_map = []
for i in range(n):
    town_map.append(list(map(int, input().split())))

town_name = []
for i in range(n):
    tmp_str_town_name = str(i)
    town_name.append(tmp_str_town_name)

p = list(itertools.permutations(town_name, n))

distance = 0
for i in range(len(p)):
    one_path = p[i]
    for j in range(n - 1):
        l = int(one_path[j])
        r = int(one_path[j + 1])
        lx, ly = town_map[l]
        rx, ry = town_map[r]
        distance += ((rx - lx)**2 + (ry - ly)**2) ** (1/2)

print(distance / len(p))