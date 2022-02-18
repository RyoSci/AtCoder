import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b, c = map(int, input().split())

if c % 2 == 0:
    aa = abs(a)
    bb = abs(b)
    if aa > bb:
        ans = ">"
    elif aa < bb:
        ans = "<"
    else:
        ans = "="
else:
    if a > b:
        ans = ">"
    elif a < b:
        ans = "<"
    else:
        ans = "="

print(ans)
