n = int(input())

for i in range(n):
    s = input()
    if sorted(s) == sorted("indeednow"):
        print("YES")
    else:
        print("NO")
