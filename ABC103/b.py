s = input()
t = input()

for i in range(len(s)):
    s = s[-1] + s[:len(s) - 1]
    if s == t:
        print("Yes")
        break
else:
    print("No")