a=int(input())
num=[int(i) for i in input().split()]
num_dict={}
# num_min1_dict={}
sum_num=0
for i in num:
    if i not in num_dict:
        num_dict[i]=1
    else:
        num_dict[i]+=1
# for i in range(a):
#     counter=0
#     tmp=num_dict[num[i]]-1
#     for key,value in num_dict.items():
#         if key==num[i]:
#             value=tmp
#         if value>=2:
#             counter+=int(value*(value-1)/2)
#     print(counter)
num_to_sum_dict={}
for key, value in num_dict.items():
    sum_num+=value*(value-1)/2

for key,value in num_dict.items():
    tmp=sum_num-value*(value-1)/2+(value-1)*(value-2)/2
    num_to_sum_dict[key]=tmp

for i in range(a):
    print(int(num_to_sum_dict[num[i]]))

