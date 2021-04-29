n = int(input())
users = {}
for i in range(n):
    si = input()
    if si not in users:
        users[si] = True
        print(i + 1)
