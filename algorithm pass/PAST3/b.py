n,m,q=map(int,input().split())
n_array=[set() for i in range(n)]
m_array=[n]*m

for i in range(q):
    line=list(map(int,input().split(" ")))
    if line[0]==1:
        score=0
        a,b=line
        for j in n_array[b-1]:
            score+=m_array[j-1]
        print(score)
    elif line[0]==2:
        a,b,c=line
        n_array[b-1].add(c)
        m_array[c-1]-=1