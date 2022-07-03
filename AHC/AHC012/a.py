# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

# 半径
r = 10**4

ans = []


def same_distance():
    """
    等間隔
    """
    dx = 2*r//50
    dy = 2*r//50
    now_x = -r
    now_y = -r
    y0 = 10**9
    y1 = -10**9
    x0 = 10**9
    x1 = -10**9
    # 経線を引く
    for i in range(50):
        now_x += dx
        ans.append((now_x, y0, now_x, y1))

    # 緯線を引く
    for i in range(50):
        now_y += dy
        ans.append((x0, now_y, x1, now_y))

    print(len(ans))
    for i in ans:
        print(*i)


same_distance()
