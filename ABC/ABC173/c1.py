import copy
h, w, k = map(int,input().split())
dot_map = []
result = 0

for i in range(h):
    tmp_input = list(input())
    dot_map.append(tmp_input)

for h_i in range(2 ** h):
    tmp_dot_map = copy.deepcopy(dot_map)
    for h_degit in range(h):
        if bin(h_i >> h_degit)[-1] == "1":
            tmp_dot_map[h_degit] = list("." * w)

    for w_i in range(2 ** w):
        sharp_counter = 0
        tmp_dot_map_2 = copy.deepcopy(tmp_dot_map)
        for w_degit in range(w):
            if bin(w_i >> w_degit)[-1] == "1":
                for h_draw in range(h):
                    tmp_dot_map_2[h_draw][w_degit] = "."

        for h_s in range(h):
            for w_s in range(w):
                if tmp_dot_map_2[h_s][w_s] == "#":
                        sharp_counter += 1
        if sharp_counter == k:
            result += 1
        # print(tmp_dot_map)
print(result)
