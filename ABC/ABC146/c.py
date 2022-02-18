a, b, x = map(int, input().split())
n = 10 ** 9

if a * n + b * 10 <= x:
    print(n)
else:
    n = 0
    is_first = True
    for i in range(8, -1, -1):
        for j in range(9, 0, -1):
            if a * (10 ** i) * j + b * (i + 1) <= x and is_first:
                is_first = False
                i_res = i
                n = (10 ** i) * j 
                # res = n
                # print(a * (10 ** i) * j + b * (i) , i, j, n)
                break 
            # breakを書かないことで10**8が候補に入ってしまっていた。足算すると、10**9になるが、i_resが本来の10より小さいので不適になっていた。
            else:
                if not is_first:
                    if a * (n + (10 ** i) * j) + b * (i_res + 1) <= x:
                        n += (10 ** i) * j
                        # print(n, i, j)
                        # res = n
                        break
        # print(n)
    print(n)