
"https://qiita.com/Pro_ktmr/items/16904c9570aa0953bf05"


def z_alog(s: str):
    z = [0]*len(s)
    z[0] = len(s)
    i = 1
    j = 0
    while i < len(s):
        while i + j < len(s) and s[j] == s[i + j]:
            j += 1
        z[i] = j

        if j == 0:
            i += 1
            continue

        k = 1
        while k < j and k + z[k] < j:
            z[i + k] = z[k]
            k += 1
        i += k
        j -= k
    return z
