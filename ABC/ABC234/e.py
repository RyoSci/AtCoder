import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x = [int(i) for i in input().strip()]
x_num = int("".join(map(str, x)))
n = len(x)
if n <= 2:
    print(x_num)

else:
    ans = int("9"*n)
    # 最上位が同じ数なら
    tmp = [0]*n
    tmp[0] = x[0]
    for j in range(-9, 10, 1):
        for k in range(n-1):
            if x[k+1]-tmp[k] <= j:
                tmp[k+1] = tmp[k]+j
            else:
                break
        else:
            tmp_num = int("".join(map(str, tmp)))
            if tmp_num >= x_num:
                ans = min(ans, tmp_num)
    # 最上位が違う数なら
    for i in range(x[0]+1, 10):
        tmp = [0]*n
        tmp[0] = i
        for j in range(-9, 10, 1):
            for k in range(n-1):
                if 0 <= tmp[k]+j <= 9:
                    tmp[k+1] = tmp[k]+j
                else:
                    break
            else:
                tmp_num = int("".join(map(str, tmp)))
                if tmp_num >= x_num:
                    ans = min(ans, tmp_num)

    print(ans)
