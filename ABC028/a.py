n = int(input())
res = ""
if n < 60:
    res = "Bad"
elif n < 90:
    res = "Good"
elif n < 100:
    res = "Great"
else:
    res = "Perfect"

print(res)
