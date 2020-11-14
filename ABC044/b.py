w = input()
alphabet_map = dict()
for i in range(26):
    alphabet_map[chr(ord("a") + i)] = 0

for i in w:
    alphabet_map[i] += 1

for value in alphabet_map.values():
    if value % 2 == 1:
        print("No")
        break
else:
    print("Yes")
