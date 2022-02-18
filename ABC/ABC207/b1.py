a, b, c, d = map(int, input().split())

for i in range(1, 10**6):
    if a+i*b <= i*c*d:
        print(i)
        exit()
else:
    print(-1)
