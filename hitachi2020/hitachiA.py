a=input()
# a="hihihsi"
for i in range(0,len(a),2):
    if a[i:i+2]=="hi":
        continue
    else:
        print("No")
        break
else:
    print("Yes")