n = int(input())
r = input()

sum_ = 0
for i in r:
    if i == "F":
        continue
    sum_ += 4 - (ord(i) - ord("A"))

print(sum_ / n)
