n = input()
res = ""
for i in range(len(n)):
    if n[i] == "1":
        res += "9"
    else:
        res += "1"
print(int(res))