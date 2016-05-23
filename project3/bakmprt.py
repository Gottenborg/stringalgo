from epm import *
#import exactPatteren as ep
import matplotlib.pyplot as plt

stri = GenerateString(1560, 5)
patt = GenerateString(5, 5)

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

# ### Random running time:
# bAt = []
# kmpt = []

# for n in range(10, 100000, 40):
#     stri = GenerateString(n, 4)
#     patt = GenerateString(4, 4)

#     bAt.append([n, timeIt("borderSearch(stri, patt)", 0, False)])
#     kmpt.append([n, timeIt("kmpSearch(stri, patt)", 0, False)])


# bAx = [x for [x, y] in bAt]
# bAy = [y/(x+4) for [x, y] in bAt]

# plt.plot(bAx, bAy)
# plt.savefig('bArandomS.png', bbox_inches='tight')

# bAy = [y for [x, y] in bAt]

# plt.figure()
# plt.plot(bAx, bAy)
# plt.savefig('bArandom.png', bbox_inches='tight')

# kmpx = [x for [x, y] in kmpt]
# kmpy = [y for [x, y] in kmpt]

# plt.plot(kmpx, kmpy)
# plt.savefig('kmprandom.png', bbox_inches='tight')

# kmpy = [y/(x+4) for [x, y] in kmpt]

# plt.figure()
# plt.plot(kmpx, kmpy)
# plt.savefig('kmprandomS.png', bbox_inches='tight')

# ### All match
# bAta = []
# kmpta = []

# for n in range(10, 100000, 40):
#     stri = GenerateString(n, 1)
#     patt = GenerateString(4, 1)

#     bAta.append([n, timeIt("borderSearch(stri, patt)", 0, False)])
#     kmpta.append([n, timeIt("kmpSearch(stri, patt)", 0, False)])

# ### All mis-match
# bAtm = []
# kmptm = []

# for n in range(10, 100000, 40):
#     stri = GenerateString(n, 1)
#     patt = GenerateString(4, 1, 1)

#     bAtm.append([n, timeIt("borderSearch(stri, patt)", 0, False)])
#     kmptm.append([n, timeIt("kmpSearch(stri, patt)", 0, False)])
    
# bAx = [x for [x, y] in bAt]
# bAy = [y/(x+4) for [x, y] in bAt]
# bAya = [y/(x+4) for [x, y] in bAta]
# bAym = [y/(x+4) for [x, y] in bAtm]

# plt.plot(bAx, bAy, label="Random")
# plt.plot(bAx, bAya, label="All match")
# plt.plot(bAx, bAym, label="All mismatch")
# plt.savefig('bAallS.png', bbox_inches='tight')

# bAy = [y for [x, y] in bAt]
# bAya = [y for [x, y] in bAta]
# bAym = [y for [x, y] in bAtm]

# plt.figure()
# plt.plot(bAx, bAy, label="Random")
# plt.plot(bAx, bAya, label="All match")
# plt.plot(bAx, bAym, label="All mismatch")
# plt.savefig('bAall.png', bbox_inches='tight')

# kmpx = [x for [x, y] in kmpt]
# kmpy = [y for [x, y] in kmpt]
# kmpya = [y for [x, y] in kmpta]
# kmpym = [y for [x, y] in kmptm]

# plt.figure()
# plt.plot(kmpx, kmpy, label="Random")
# plt.plot(kmpx, kmpya, label="All match")
# plt.plot(kmpx, kmpym, label="All mismatch")
# plt.savefig('kmpall.png', bbox_inches='tight')

# kmpy = [y/(x+4) for [x, y] in kmpt]
# kmpya = [y/(x+4) for [x, y] in kmpta]
# kmpym = [y/(x+4) for [x, y] in kmptm]

# plt.figure()
# plt.plot(kmpx, kmpy, label="Random")
# plt.plot(kmpx, kmpya, label="All match")
# plt.plot(kmpx, kmpym, label="All mismatch")
# plt.savefig('kmpallS.png', bbox_inches='tight')

import epm
import matplotlib.pyplot as plt
import bwt 


# ### Random running time:
bAt = []
kmpt = []
bwtt = []
naivet = []

stri = GenerateString(10000, 4)
patt = GenerateString(4, 4)

#timeIt("epm.borderSearch(stri, patt)", 0)
#timeIt("epm.kmpSearch(stri, patt)", 0)
#timeIt("bwt.bwt_search(stri, patt)", 0)
#timeIt("epm.naiveSearch(stri, patt)", 0)

for n in range(10, 10000, 40):
    stri = GenerateString(n, 4)
    patt = GenerateString(4, 4)

    bAt.append([n, timeIt("epm.borderSearch(stri, patt)", 0, False)])
    kmpt.append([n, timeIt("epm.kmpSearch(stri, patt)", 0, False)])
    Sarray = bwt.suffix_array(stri+"$")
    bwtt.append([n, timeIt("bwt.bwt_search(stri+'$', patt, Sarray)", 0, False)])
    naivet.append([n, timeIt("epm.naiveSearch(stri, patt)", 0, False)])

bAx = [x for [x, y] in bAt]
bAy = [y for [x, y] in bAt]
kmpy = [y for [x, y] in kmpt]
bwty = [y for [x, y] in bwtt]
naivey = [y for [x, y] in naivet]

plt.plot(bAx, bAy, label="Border Array")
plt.plot(bAx, kmpy, label="KMP")
plt.plot(bAx, bwty, label="BWT")
plt.plot(bAx, naivey, label="Naive")
plt.savefig('BWT.png', bbox_inches='tight')
