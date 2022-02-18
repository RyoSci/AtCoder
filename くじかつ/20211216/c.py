import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x, y, a, b = list(map(int, input().split()))
ans = 0

if x*a >= x+b:
    ans += (y-x)//b
    if (y-x) % b == 0:
        ans -= 1
    print(ans)
else:
    now = x
    for i in range(1, 100):
        if now*a <= now+b:
            if now*a < y:
                now *= a
                ans += 1
            else:
                break
        else:
            if now+b < y:
                ans += (y-now)//b
                if (y-now) % b == 0:
                    ans -= 1
                break
            else:
                break
    print(ans)
