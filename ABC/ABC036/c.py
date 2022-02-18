n = int(input())
a = [int(input()) for i in range(n)]
num_map = dict()

for i in range(n):
    if a[i] not in num_map:
        num_map[a[i]] = 1

keys = sorted(list(num_map.keys()))
for i in range(len(keys)):
    num_map[keys[i]] = i

for i in range(n):
    print(num_map[a[i]])
