def timeIt(code, iterations=4, toprint=True):
    from time import time
    st = time()
    if iterations>6: raise("Node: iterations is 10 to power of iterations.")
    for i in range(10**iterations):
        exec code
    thetime = time()-st
    if(toprint==True): print("----- It took %.5f seconds to run: %s with %d iterations -----" %
          (thetime, code, 10**iterations))
    return thetime

def suffix_array(string):
    SA12 = sorted([i for i in range(len(string)) if i % 3 != 0], key=lambda i: string[i:i+4])
    SA0 = sorted([i for i in range(len(string)) if i % 3 == 0], key=lambda i: string[i:i+4])

    n, m = len(SA12), len(SA0)
    i, j = 0, 0

    a = []
    
    while i<n and j<m:
        if SA12[i] % 3 == 0:
            if string[SA12[i]]>string[SA0[j]]:
                a.append(SA12[i])
                i += 1
            if string[SA12[i]]<string[SA0[j]]:
                a.append(SA0[j])
                j += 1
            continue
        if SA12[i] % 3 == 1:
            if string[SA12[i]:SA12[i]+2]>string[SA0[j]:SA0[j]+2]:
                a.append(SA12[i])
                i += 1
            if string[SA12[i]:SA12[i]+2]<string[SA0[j]:SA0[j]+2]:
                a.append(SA0[j])
                j += 1
            continue
        if SA12[i] % 3 == 2:
            if string[SA12[i]:SA12[i]+3]>string[SA0[j]:SA0[j]+3]:
                a.append(SA12[i])
                i += 1
            if string[SA12[i]:SA12[i]+3]<string[SA0[j]:SA0[j]+3]:
                a.append(SA0[j])
                j += 1
            continue

    if i<n: a = a + SA12[i:]
    if j<m: a = a + SA12[j:]
        
    return a

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


# V2 suffix array outside:

def bwt_search(x, p, S):
    
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
