n = int(input())
s = input()
st = []

for i in s:
    if i == ")":
        if len(st) == 0 or st[-1] == ")":
            st.append(")")
        else:
            st.pop()
    else:
        st.append("(")

h = ""
t = ""
for i in st:
    if i == ")":
        h += "("
    else:
        t += ")"

print(h+s+t)
