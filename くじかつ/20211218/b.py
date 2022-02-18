import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b, c = list(map(int, input().split()))

for i in range(10**6):
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        a, b, c = b//2+c//2, c//2+a//2, a//2+b//2
    else:
        print(i)
        break
else:
    print(-1)
