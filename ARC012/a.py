week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day = week.index(input())

ans = (6 - day) % 6
print(ans)
