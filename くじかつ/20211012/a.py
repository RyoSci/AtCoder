import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a = list(map(int, input().split()))
a.sort()
if a[1]-a[0] == a[2]-a[1]:
    print("Yes")

else:
    print("No")
