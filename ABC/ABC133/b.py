import math
n , d = map(int, input().split())
x = []
for i in range(n):
    line = list(map(int, input().split()))
    x.append(line)

counter = 0
for i in range(n):
    for j in range(i + 1, n):
        distance = 0
        for k in range(d):
            distance += (x[i][k] - x[j][k]) ** 2
        distance = math.sqrt(distance)
        if distance == int(distance):
            counter += 1
print(counter)