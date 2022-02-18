import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
dis = 0
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append(a+b+a)
    dis += a

ab.sort(reverse=True)
cnt = 0
for i in range(n):
    if dis < 0:
        break
    else:
        cnt += 1
        dis -= ab[i]

print(cnt)
