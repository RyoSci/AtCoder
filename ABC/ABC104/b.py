s = input()
ans = True
if s[0] != "A":
    ans = False

c = 0
for i in range(2, len(s) - 1):
    if s[i] == "C":
        c += 1
if c != 1:
    ans = False

a = 0
c = 0
for i in s:
    if i == "A":
        a += 1
    elif i == "C":
        c += 1
    elif not (ord("a") <= ord(i) <= ord("z")):
        ans = False
        break

if ans and a == 1 and c == 1:
    print("AC")
else:
    print("WA")
