import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
ball_nums = [0]*m
now_balls = [0]*m
boxes = []
for i in range(m):
    k = int(input())
    ball_nums[i] = k
    a = list(map(int, input().split()))
    boxes.append(a)

d = dict()
ball = 2*n
nexts = deque()

for i in range(m):
    if boxes[i][now_balls[i]] not in d:
        d[boxes[i][now_balls[i]]] = i
    else:
        nexts.append(d[boxes[i][0]])
        nexts.append(i)
        boxid = d[boxes[i][now_balls[i]]]
        del d[boxes[i][0]]
        ball -= 2

while len(nexts) > 0:
    next = nexts.popleft()
    if now_balls[next]+1 < ball_nums[next]:
        now_balls[next] += 1
        if boxes[next][now_balls[next]] not in d:
            d[boxes[next][now_balls[next]]] = next
        else:
            nexts.append(d[boxes[next][now_balls[next]]])
            nexts.append(next)
            del d[boxes[next][now_balls[next]]]
            ball -= 2


if ball == 0:
    print("Yes")
else:
    print("No")
