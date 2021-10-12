import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = input().split()
c = int(a+b)
for i in range(10**4):
    if i**2 == c:
        print("Yes")
        exit()
else:
    print("No")
