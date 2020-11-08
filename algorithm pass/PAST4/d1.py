n = int(input())
s = input()
s_sharp = [i for i in range(n) if s[i] == "#"]
sum_x_y = 100
ans = (0, 0)
for x in range(n):
    for y in range(n):
        for i in range(n):
            if s[i] == ".":
                for j in s_sharp:
                    if (i < j and i + x >= j) or (j < i and i - y <= j):
                        break
                else:
                    break
        else:
            if sum_x_y > x + y:
                sum_x_y = x + y
                ans = (x, y)

print(*ans)
