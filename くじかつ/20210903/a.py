import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x, y = map(int, input().split("."))
x = str(x)
if y <= 2:
    print(x+"-")
elif y <= 6:
    print(x)
else:
    print(x+"+")
