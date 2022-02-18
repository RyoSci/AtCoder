# a=input()
a="1817181712114"
num=len(a)
mod_map={0:1}
moji_int=0
for i in range(-1,-num-1,-1):
    moji_int+=int(a[i])*10**(-i-1)
    # mod=int(a[i:])%2019
    mod=moji_int%2019
    if mod not in mod_map:
        mod_map[mod]=1
    else:
        mod_map[mod]+=1
    # print(mod)

    # print(int(a[i:]))
    # print(a[i])

res=0
for i in mod_map.values():
    res+=int(i*(i-1)/2)
print(res)