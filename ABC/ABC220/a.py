import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b, c = map(int, input().split())

for i in range(a, b+1):
    if i % c == 0:
        print(i)
        exit()
else:
    print(-1)
