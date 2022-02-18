import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s, t, x = list(map(int, input().split()))
if s < t:
    if s <= x < t:
        print("Yes")
    else:
        print("No")
else:
    if s <= x < 24 or 0 <= x < t:
        print("Yes")
    else:
        print("No")
