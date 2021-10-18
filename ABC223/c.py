import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
t = 0
ab = []
for i in range(n):
    a, b = map(int, input().split())
    t += a/b
    ab.append([a, b])

now_t = 0
l = 0
for i in range(n):
    if now_t+ab[i][0]/ab[i][1] <= t/2:
        l += ab[i][0]
        now_t += ab[i][0]/ab[i][1]
    else:
        time = t/2-now_t
        dis = ab[i][1]
        # l += (t/2-now_t)*(ab[i][0]/ab[i][1])
        l += time*dis
        break

print(l)
