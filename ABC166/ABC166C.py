tenboudai,roads_num=map(int,input().split())
t_heights=list(map(int,input().split()))
t_points=list(range(tenboudai))
for i in range(roads_num):
    ai,bi=map(int,input().split())
    ai-=1
    bi-=1
    if t_heights[ai]>t_heights[bi]:
        t_points[bi]=t_points[ai]
    elif   t_heights[bi]>t_heights[ai]:
        t_points[ai]=t_points[bi]
    else:
        t_points[ai]=-1
        t_points[bi]=-1
counter=0
for i in range(tenboudai):
    if t_points[i]==i:
        counter+=1
print(counter)
