import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x, y = input().split(".")
y = int(y)
if 0 <= y <= 2:
    print(x+"-")
elif 3 <= y <= 6:
    print(x)
else:
    print(x+"+")
