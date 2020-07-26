n = int(input())
s = input()

for i in range(1, n):
    if s[0] == s[i] and s[:i] == s[i:]:
        print("Yes")
        break
else:
    print("No")