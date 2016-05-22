def borderArray(x):

    n = len(x)
    x = "#"+x
    B = [0 for i in xrange(n+1)]

    for i in xrange(1,n):
        b = B[i]
        while b>0 and x[i+1]!=x[b+1]:
            b = B[b]
        if x[i+1]==x[b+1]:
            B[i+1] = b+1
        else:
            B[i+1] = 0

    return B[1:]

def borderSearch(x, p):

    B = borderArray(p + "$" + x)
    m = len(p)
    occ = []

    for i in xrange(len(B)):
        if B[i]==m:
            occ.append(i-2*m)

    return occ

def naiveSearch(x, p):

    n, m = len(x), len(p)
    occ = []

    for i in xrange(n-m+1):
        j = 0
        while j<m and x[i+j]==p[j]:
            j += 1
        if j==m:
            occ.append(i)

    return occ

def kmpSearch(x, p):

    n, m = len(x), len(p)
    B = [0]+borderArray(p)
    i, j = 0, 0
    occ = []

    while i <= n-m+j:
        
        while j <= m-1 and x[i]==p[j]:
            i, j = i+1, j+1

        if j==m:
            occ.append(i-m)
        if j==0: i = i+1
        else: j = B[j]
        
    return occ

string = "abcabcabcabc"
pattern = "abc"

print "String:", string
print "Pattern:", pattern

print "Border Array search:", borderSearch(string, pattern)
print "Naive search:", naiveSearch(string, pattern)
print "Kmp search:", kmpSearch(string, pattern)


def collectPatterns(l, x, p):
    m = len(p)
    r = []

    for i in l:
        r.append((i, x[i:i+m]))

    return r

string = "abababababababaababababababab"
pattern = "abababababa"

print "String:", string
print "Pattern:", pattern

bs = borderSearch(string, pattern)
print "Border Array search:", collectPatterns(bs, string, pattern)
ns = naiveSearch(string, pattern)
print "Naive search:", collectPatterns(ns, string, pattern)
ks = kmpSearch(string, pattern)
print "Kmp search:", collectPatterns(ks, string, pattern)

print borderSearch("Hello there. Hello!", "Hello")
print naiveSearch("Hello there. Hello!", "Hello")
print kmpSearch("Hello there. Hello!", "Hello")


def GenerateString(n, a, offset=0):

    import random
    
    alphabet = [chr(65+i+offset) for i in xrange(a)]

    s = []
    
    for i in xrange(n):
        s.append(alphabet[random.randint(0, a-1)])

    return "".join(s)

print GenerateString(50, 1)
print GenerateString(5, 1, 1)
