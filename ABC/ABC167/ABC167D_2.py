n,k=map(int,input().split())
teleport=list(map(int,input().split()))
double_counter=set()
# mojiretu="1"
mojiretu=["1"]
index=1
double_counter.add(index)
flag=False
for i in range(k):
    tmp=teleport[index-1]
    if tmp in double_counter:
        flag=True
        break
    else:
        double_counter.add(tmp)
        # mojiretu+=str(tmp)
        mojiretu.append(str(tmp))
        index=tmp
else:
    print(tmp)

if flag:
    #mojiretu is string
    index=mojiretu.index(str(tmp))
    loop_str=mojiretu[index:]
    length=k%len(loop_str)-len(mojiretu[:index])%len(loop_str)
    print(loop_str[length])

    #mojiretu is list
    index = mojiretu.index(str(tmp))
    loop_str=mojiretu[index:]
    length=k%len(loop_str)-len(mojiretu[:index])%len(loop_str)
    print(loop_str[length])
