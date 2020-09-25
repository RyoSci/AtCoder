s = input()
base_str = "WBWBWWBWBWBW"
rank_index = [0, 2, 4, 5, 7, 9, 11]
rank_name = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]
for i in range(7):
    res_str = base_str[rank_index[i]:] + base_str[:rank_index[i]]
    if res_str == s[:12]:
        print(rank_name[i])
