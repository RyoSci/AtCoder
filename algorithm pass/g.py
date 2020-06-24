n,x,y=map(int,input().split())
import queue
block=set()
for i in range(n):
    line=set(map(int,input().split()))
    block.add(line)

q=queue.Queue()
q.put((0,0))
already=set()
already.add((0,0))

while not q.empty():
    tmp=q.get()
    for 