# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
w = int(input())
w = 10**6+1
goods = [0]*(w+1)
goods[0] = 1
ans = []
cnt = 1


def f(cnt):
    global ans, goods
    tmp_goods = []
    n = len(ans)
    if not (cnt <= w and goods[cnt] == 0):
        return False
    tmp_goods.append(cnt)
    for i in range(n):
        s = cnt+ans[i]
        # if not (s <= w and goods[s] == 0):
        if s <= w:
            if not (goods[s] == 0):
                return False
            tmp_goods.append(s)
        for j in range(i+1, n):
            s = cnt+ans[i]+ans[j]
            # if not (s <= w and goods[s] == 0):
            if s <= w:
                if not (goods[s] == 0):
                    return False
                tmp_goods.append(s)
    for i in tmp_goods:
        goods[i] = 1
    return True


for cnt in range(1, 10**6+1):
    if f(cnt):
        ans.append(cnt)

print(len(ans))
print(*ans)

print(sum(goods[:w]))
