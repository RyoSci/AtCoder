n = int(input())
red = []
white = []
s = input()

for i in range(n):
    if s[i] == "R":
        red.append(i)
    else:
        white.append(i)

roop_min_num = min(len(red), len(white))

res = 0
for i in range(roop_min_num):
    if white[i] < red[-i - 1]:
        res += 1
print(res)
