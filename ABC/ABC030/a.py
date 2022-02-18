a, b, c, d = map(int, input().split())
if b * c > a * d:
    print("TAKAHASHI")
elif b * c == a * d:
    print("DRAW")
else:
    print("AOKI")
