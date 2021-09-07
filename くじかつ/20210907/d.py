import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

b, c = map(int, input().split())

res = 0
if b > 0:
    bm = -b
    end1 = bm-(c-1)//2
    if (c-1) % 2 == 0:
        res += max(0, (bm-end1)*2-1)
    else:
        res += (bm-end1)*2
    end2 = b-c//2
    if end2 <= 0:
        res += b*2+1
    else:
        if c % 2 == 0:
            res += max(0, (b-end2+1)*2-1)
        else:
            res += (b-end2+1)*2
else:
    bm = -b
    end1 = b-c//2
    if c % 2 == 0:
        res += (max(0, b-end1)*2-1)
    else:
        res += (b-end1)*2
    end2 = bm-(c-1)//2
    if end2 <= 0:
        res += bm*2+1
    else:
        if (c-1) % 2 == 0:
            res += max(0, (bm-end2+1)*2-1)
        else:
            res += (bm-end2+1)*2

print(res)
