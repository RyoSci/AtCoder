n = int(input())
a = sorted(list(map(int, input().split())))

q = int(input())
b = [[int(input()), _] for _ in range(q)]
b.sort(key=lambda x: x[0])

ans = [0] * q
j = 0
for i in range(q):
    dis = abs(a[j] - b[i][0])
    while j < n:
        if dis < abs(a[j] - b[i][0]):
            j -= 1
            break
        else:
            dis = abs(a[j] - b[i][0])
        j += 1
    if j == n:
        j -= 1
    ans[b[i][1]] = dis

for i in range(q):
    print(ans[i])
