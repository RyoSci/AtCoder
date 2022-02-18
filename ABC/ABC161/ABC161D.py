from queue import Queue
k = int(input())
ans = 0
q = Queue()
for i in range(1, 10):
    q.put(str(i))

while 1:
    a = q.get()
    ans += 1
    if ans == k:
        print(a)
        break
    if a[-1] != "0":
        q.put(a + str(int(a[-1]) - 1))
    q.put(a + str(int(a[-1])))
    if a[-1] != "9":
        q.put(a + str(int(a[-1]) + 1))
