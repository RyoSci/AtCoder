n,m,q=map(int,input().split())
taiouhyou=[set() for i in range(n+1)]


for i in range(m):
    u,v=map(int,input().split())
    taiouhyou[u].add(v)
    taiouhyou[v].add(u)

color_list=list(map(int,input().split()))

for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        print(color_list[query[1]-1])
        for j in taiouhyou[query[1]]:
            color_list[j-1]=color_list[query[1]-1]
    else:
        print(color_list[query[1]-1])
        color_list[query[1]-1]=query[2]

