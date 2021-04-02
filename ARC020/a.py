a, b = map(lambda x: abs(int(x)), input().split())
if a < b:
    print("Ant")
elif a > b:
    print("Bug")
else:
    print("Draw")
