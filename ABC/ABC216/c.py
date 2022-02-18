import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

ans = ""
while n > 0:
    if n % 2 == 1:
        ans += "A"
        n -= 1
    else:
        ans += "B"
        n //= 2

print(ans[::-1])
