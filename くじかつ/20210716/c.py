k, a, b = map(int, input().split())

if a+2 < b:
    tmp = k-(a-1)
    res = max(k+1, a+tmp//2*(b-a)+tmp % 2)
    print(res)
else:
    print(1+k)
