s = input()

max_length = 0
counter = 0
for i in range(len(s)):
    if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
        counter += 1
    else:
        max_length = max(max_length, counter)
        counter = 0
max_length = max(max_length, counter)

print(max_length)
