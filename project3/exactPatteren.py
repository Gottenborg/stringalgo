import sys

def stringreader(filename):
    with open(filename) as f:
        string = f.read()
    return string


def naive(text, pattern):
    lengthOfText = len(text)
    lengthOfPattern = len(pattern)
    matchAt = []
    for i in xrange(0, lengthOfText-lengthOfPattern+1):
        Matching = True
        for j in xrange(lengthOfPattern):
            if text[i+j-1] != pattern[j]:
                Matching = False
                break
        if Matching == True:
            matchAt.append(i)
            print matchAt
    return matchAt


def KMPPrefix(pattern):
    lengthOfPattern = len(pattern)
    prefixTable = [0]
    i = 0
    for j in xrange(2, lengthOfPattern):
        while i > 0 and pattern[i+1] != pattern[j]:
            i = prefixTable[i]
        if pattern[i+1] == pattern[j]:
            i = i + 1
        prefixTable.append(i)
    return prefixTable



def KMPMatching(text, pattern, prefixTable):
    prefixTable = prefixTable
    print prefixTable
    lengthOfText = len(text)
    lengthOfPattern = len(pattern)
    matchAt = []
    i=0
    j=0
    k=0
    while lengthOfText-k > lengthOfPattern:
        while j < lengthOfPattern and text[i] == pattern[j]:
            i = i+1
            j = j+1
            print "j %s" %j
        if j >= lengthOfPattern:
            print "Goal"
            matchAt.append(k)
        if prefixTable[j-1] > 0:
            k = i - prefixTable[j-1]
        elif k == i:
            i = i+1
        k = i
        print k
        if j > 0:
            j = prefixTable[j-1]+1
    print "matchAt %s" %(matchAt)
    return matchAt

if __name__ == "__main__":
    text = "cocacolaocaaawaaafcocacola"
    pattern = "cocacola"
    naive(text, pattern)
    pattern2 = "$" + pattern
    prefixTable = KMPPrefix(pattern2)
    KMPMatching(text, pattern, prefixTable)