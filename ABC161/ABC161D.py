# k=int(input())
# counter=12
# if k<=12:
#     print(k)
# else:
#     for i in range(13,3234566667+1):
#         tmp=str(i)
#         for j in range(len(tmp)-1):
#             if abs(int(tmp[j])-int(tmp[j+1]))>1:
#                 break
#         else:
#             counter+=1
#         if counter==k:
#             print(i)
#             break
# a=reversed(input())
a=input()
num=len(a)
mod_map={0:1}
# mod_list=[1]+[0]*2019
moji_int=0
Sn=[0]*(num+1)
Sn=0
tens=[1]*(num+1)
# tens=1
for i in range(-1,-num-1,-1):
# for i in a:
    tens[-i]=tens[-i-1]*10%2019
    tmp=int(a[i])*(tens[-i-1])
    # tmp=int(i)*(tens)
    Sn[-i]=(Sn[-i-1]+tmp)%2019
    # Sn=(Sn+tmp)%2019
    mod=Sn[-i]
    # tens=tens*10%2019
    # mod_list[mod]+=1
    if mod not in mod_map:
        mod_map[mod]=1
    else:
        mod_map[mod]+=1

# for i in range(-1,-num-1,-1):
#     moji_int+=int(a[i])*(10**(-i-1)%2019)
#     mod=moji_int%2019
#     if mod not in mod_map:
#         mod_map[mod]=1
#     else:
#         mod_map[mod]+=1

res=0
for i in mod_map.values():
    res+=int(i*(i-1)/2)
# for i in mod_list:
#     res+=int(i*(i-1)/2)
print(res)
# print(Sn)
# print(tens)   
# print(mod_map)     