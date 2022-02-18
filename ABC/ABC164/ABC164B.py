t_hp,t_ap,a_hp,a_ap=map(int,input().split())
if t_hp%a_ap==0:
    tp=t_hp//a_ap
else:
    tp=t_hp//a_ap+1
if a_hp%t_ap==0:
    ap=a_hp//t_ap
else:
    ap=a_hp//t_ap+1

if ap<=tp:
    print("Yes")
else:
    print("No")