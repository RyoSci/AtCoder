n = int(input())
a = []
b = []
dis = 0
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    dis += bi - ai

start_res = 10 ** 12
goal_res = 10 ** 12
for i in range(n):
    start_tmp = 0
    goal_tmp = 0
    start = a[i]
    goal = b[i]
    for j in range(n):
        start_tmp += abs(start - a[j])
        goal_tmp += abs(goal - b[j])
    start_res = min(start_res, start_tmp)
    goal_res = min(goal_res, goal_tmp)

print(start_res + goal_res + dis)
