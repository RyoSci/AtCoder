import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a = sorted(list(map(int, input().split())))
c = a[1]-a[0]
d = a[2]-a[1]

if c >= d:
    print(c-d)
else:
    print((c+d+1)//2-c+(c+d) % 2)
