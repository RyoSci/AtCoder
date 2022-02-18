a, b = map(int, input().split())

if a <= 0 <= b:
    print("Zero")
elif b < 0:
    if (b - a + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")
elif 0 < a:
    print("Positive")
