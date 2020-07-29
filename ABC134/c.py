n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a_copy = a[::]
a_copy.sort(reverse=True)

for i in range(n):
    if a[i] != a_copy[0]:
        print(a_copy[0])
    else:
        print(a_copy[1])