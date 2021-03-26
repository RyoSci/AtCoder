b = list(map(int, input().split()))
n = int(input())
a2b = [0] * 10

for i in range(10):
    a2b[b[i]] = i

b_a_list = []
for i in range(n):
    a = input()
    bnum = ""
    for j in a:
        bnum += str(a2b[int(j)])
    b_a_list.append([int(bnum), int(a)])

b_a_list.sort(key=lambda x: x[0])

for i in range(n):
    print(b_a_list[i][1])
