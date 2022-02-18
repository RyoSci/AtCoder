n,k=map(int,input().split())
an_list=list(map(int,input().split()))

position=1
if k<2*10**5:
    for i in range(k):
        position=an_list[position-1]
    print(position)
else:
    position=1
    break_flag=False
    count_set=set()
    count_set.add(1)
    first_str="1"
    loop_str=""
    position=1
    for i in range(k): #これだけ回せば必ず繰り返し、今はk＞nであることがわかっている。
        position=an_list[position-1]
        first_str+=str(position)
        if position in count_set:
            # loop_first=position
            # tmp=position
            loop_str+=str(position)
            # position=an_list[position-1]
            
            # while True:
            # position=an_list[position-1]
            if loop_str[0]==str(an_list[position-1]):
                break_flag=True
                break
            # loop_str+=str(position)
            # position=tmp   
        else:
            count_set.add(position)
        if break_flag:
            break
    # print(loop_str)
    # print(first_str)
    if break_flag:
        k-=(len(first_str)-2*len(loop_str))
        k%=len(loop_str)
        print(loop_str[k])
        # print("if")
    # else:
    #     print(first_str[-1]) #print(position) is also OK!
    #     print("else")


# n,k=map(int,input().split())
# an_list=list(map(int,input().split()))

# position=1
# break_flag=False
# count_set=set()
# count_set.add(1)
# first_str="1"
# loop_str=""
# position=1
# for i in range(k): #これだけ回せば必ず繰り返し、今はk＞nであることがわかっている。
#     position=an_list[position-1]
#     first_str+=str(position)
#     if position in count_set:
#         # loop_first=position
#         # tmp=position
#         loop_str+=str(position)
#         # position=an_list[position-1]
        
#         # while True:
#         # position=an_list[position-1]
#         if loop_str[0]==str(an_list[position-1]):
#             break_flag=True
#             break
#         # loop_str+=str(position)
#         # position=tmp   
#     else:
#         count_set.add(position)
#     if break_flag:
#         break
# print(loop_str)
# print(first_str)
# if break_flag:
#     k-=(len(first_str)-2*len(loop_str))
#     k%=len(loop_str)
#     print(loop_str[k])
#     print("if")
# else:
#     print(first_str[-1]) #print(position) is also OK!
#     print("else")
