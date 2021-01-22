n = int(input())
s = {"black": 0, "white": 0}
for i in range(n):
    s[input()] += 1

if s["black"] > s["white"]:
    print("black")
else:
    print("white")
