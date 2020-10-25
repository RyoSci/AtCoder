a, b, c, d = map(int, input().split())
if a <= c <= b or a <= d <= b or c <= a <= b <= d:
    print("Yes")
else:
    print("No")
