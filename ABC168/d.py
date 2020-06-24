import queue
n,m=map(int,input().split())
road_list=[set() for i in range(n)]
mitisirube=[0]*n
mitisirube[0]=1
for i in range(m):
    a,b=map(int,input().split())
    road_list[a-1].add(b)
    road_list[b-1].add(a)

q = queue.Queue()

counter_set=set()
counter_set.add(1)
for i in road_list[0]:
    q.put(i)
    mitisirube[i-1]=1
    counter_set.add(i)

while not q.empty():
# j=0
# while j<100:
    tmp=q.get()
    for i in road_list[tmp-1]:
        if i not in counter_set:
            q.put(i)
            counter_set.add(i)
            if mitisirube[i-1]==0:
                mitisirube[i-1]=tmp
    # j+=1    
# print(road_list)
# print(mitisirube)
if mitisirube.count(0)>0:
    print("No")
else:
    print("Yes")
    for i in range(1,len(mitisirube)):
        print(mitisirube[i])