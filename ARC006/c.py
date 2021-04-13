n = int(input())
st = [10 ** 5]
for i in range(n):
    w = int(input())
    min_j = 10 ** 5 + 1
    index = None
    for id, j in enumerate(st):
        if w <= j and j < min_j:
            index = id
            min_j = j
    if index is not None:
        st[index] = w
    else:
        st.append(w)

print(len(st))
