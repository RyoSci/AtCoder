s = set(input())

for i in range(26):
    if chr(i + ord("a")) not in s:
        print(chr(i + ord("a")))
        break
else:
    print("None")
