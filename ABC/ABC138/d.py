from queue import Queue
n, q = map(int, input().split())
par2chi = [[] for i in range(n)]
counter = [0] * n

for i in range(n - 1):
    a, b = map(int, input().split())
    par2chi[a - 1].append(b - 1)
    par2chi[b - 1].append(a - 1)

for i in range(q):
    p, x = map(int, input().split())
    counter[p - 1] += x

q = Queue()
children = [0, tuple(set(par2chi[0]))]
q.put(children)

memo = set()
while not q.empty():
    pair, children = q.get()
    for child in children:
        if child in memo:
            continue
        counter[child] += counter[pair]
        if par2chi[child] != []:
            q.put([child, tuple(set(par2chi[child]))])
    memo.add(pair)
print(*counter)
# print(par2chi)
