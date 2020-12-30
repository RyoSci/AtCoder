from queue import Queue
k = int(input())

q = Queue()
for i in range(1, 10):
    q.put(i)

ans = 9


def break_checker(a):
    global ans
    ans += 1
    if ans == k:
        print(a)
        exit()
    else:
        q.put(a)


if k <= 9:
    print(k)
    exit()

while 1:
    a = q.get()
    for i in range(-1, 2, 1):
        if 0 <= a % 10 + i <= 9:
            break_checker(a * 10 + a % 10 + i)
