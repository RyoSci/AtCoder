n = int(input())
b = list(map(int, input().split()))

# error_input_examples
# b = [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]

flag = True
for i in range(n):
    if b[i] > i + 1:
        flag = False
        break

if flag:
    res = []
    while len(b) != 0:
        last_insert = 0
        for i in range(len(b) - 1, -1, -1):
            if b[i] == i + 1:
                last_insert = b[i]
                res.append(last_insert)
                del b[i]
                break

    for i in range(n - 1, -1, -1):
        print(res[i])

else:
    print(-1)
