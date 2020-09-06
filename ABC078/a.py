x, y = map(ord, input().split())
if x > y:
    print(">")
elif x == y:
    print("=")
else:
    print("<")
