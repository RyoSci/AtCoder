import sys
input = sys.stdin.readline
num,display=map(int,input().split())
length=0
counter=0
num_list=[int(input()) for i in range(num)]
for i in range(num-1):
    if num_list[i]<num_list[i+1]:
        length+=1
        if length>=display-1:
            counter+=1
    else:
        length=0
if display==1:
    print(len(num_list))
else:
    print(counter)

