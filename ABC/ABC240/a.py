import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = map(int, input().split())
if a+1==b or (b%10+1)==a:
    print("Yes")
else:
    print("No")