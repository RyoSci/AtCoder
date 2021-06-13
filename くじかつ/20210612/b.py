n = int(input())
d = dict()
array = []
for i in range(n):
    s = input()
    d[s] = 1
    array.append(s)

ans = "satisfiable"
for i in range(n):
    if "!" + array[i] in d:
        ans = array[i]
        break

print(ans)
