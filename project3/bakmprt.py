from epm import *
#import exactPatteren as ep
import matplotlib.pyplot as plt

print "\n\n\n\n\n\n\n"

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

### Random running time:
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
