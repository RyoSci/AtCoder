s = []
for i in range(4):
    s.append(input())

s.sort()
ans = ["H", "2B", "3B", "HR"]
ans.sort()

if s == ans:
    print("Yes")
else:
    print("No")
