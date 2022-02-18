import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)
else:
    print(0)
