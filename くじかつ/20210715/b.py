t = int(input())


def cal(x):
    return x*(x+1)//2


for i in range(t):
    l, r = map(int, input().split())
    x = (r-l)-l+1
    if 0 <= x:
        print(cal(x))
    else:
        print(0)
