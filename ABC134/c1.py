n = int(input())
a = []
top = 1
two = 1
for i in range(n):
    line = int(input())
    a.append(line)
    if line >= top:
        top, two = line, top
    elif line >= two:
        two = line

for i in range(n):
    if a[i] != top:
        print(top)
    else:
        print(two)