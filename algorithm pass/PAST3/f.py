n=int(input())
array=[None]*n

for i in range(n):
    line=set(input())
    array[i]=line

if len(array)%2==0:
    num=len(array)//2
else:
    num=(len(array)-1)//2

string=""
breakflag=False
for i in range(num):
    for j in array[i]:
        if j in array[-i-1]:
            string+=j
            break
    else:
        breakflag=True
    
    if breakflag:
        break

if breakflag:
    print(-1)
else:
    if len(array)%2==0:
        print(string+string[::-1])
    else:
        print(string+list(array[num])[0]+string[::-1])
        