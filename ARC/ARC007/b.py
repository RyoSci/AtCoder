n, m = map(int, input().split())
cd = dict()
for i in range(n + 1):
    cd[i] = i
cd[0] = -1
out = 0
for i in range(m):
    disk = int(input())
    cd[out] = cd[disk]
    out = disk
    cd[disk] = -1

cd = [[val, key] for key, val in cd.items()]
cd.sort()
for i in cd:
    if i[0] == -1:
        continue
    print(i[1])
