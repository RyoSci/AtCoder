import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())

ans = ""
while k > 0:
    if k % 2 == 1:
        ans += "2"
    else:
        ans += "0"
    k //= 2

print(ans[::-1])
