def suffix_array(string):
    return sorted(range(len(string)), key=lambda i: string[i:])

def bwt(x, S):
    
    b = []
    for i in S:
        b.append(x[i-1])

    return b

def bwt_search(x, p):
    
    x = x+"$"
    S = suffix_array(x)
    b = bwt(x, S)

    C, l, c = {"$": 0}, x[S[0]], 0
    for i in S[1:]:
        if x[i]==l:
            c += 1
            continue
        C[x[i]] = c
        l = x[i]
        c += 1

    O = {i:[] for i in C.keys()}
    for i in b:
        for key in O:
            if i == key:
                if O[key] == []:
                    O[key].append(1)
                else:
                    O[key].append(O[key][-1]+1)
                continue
            if O[key] == []:
                O[key].append(0)
            else:
                O[key].append(O[key][-1])
    
    n, m = len(x)-1, len(p)
    L, R = 0, n
    i = m-1
    
    while i>=0 and L<=R:
        if L-1<0: L = C[p[i]]+1
        else: L = C[p[i]]+O[p[i]][L-1]+1
        R = C[p[i]]+O[p[i]][R]
        i -= 1

    occ = []
    if i<0 and L <= R:
        for j in range(L, R+1):
            occ.append(S[j])
        return occ
    else:
        return None
