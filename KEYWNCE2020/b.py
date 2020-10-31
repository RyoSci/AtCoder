n = int(input())
robot_arms = []
for i in range(n):
    x, l = map(int, input().split())
    robot_arms.append([x + l, x - l])

robot_arms.sort()
res = 1
now = robot_arms[0]
for i in range(1, n):
    if robot_arms[i][1] >= now[0]:
        res += 1
        now = robot_arms[i]

print(res)
