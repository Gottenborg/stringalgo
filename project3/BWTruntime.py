
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

import epm
import bwt
import matplotlib.pyplot as plt

text = open("walrus-and-carpenter.txt").read()

print "Walrus and carpenter, Walrus"
print "-"*30

print "Border Array", epm.borderSearch(text, "Walrus")
print "KMP", epm.kmpSearch(text, "Walrus")
print "Naive", epm.naiveSearch(text, "Walrus")
print "BWT", bwt.bwt_search(text, "Walrus")

print 
print "Walrus and carpenter, is"
print "-"*30

print "Border Array", epm.borderSearch(text, "is")
print "KMP", epm.kmpSearch(text, "is")
print "Naive", epm.naiveSearch(text, "is")
print "BWT", bwt.bwt_search(text, "is")

stri = epm.GenerateString(5000, 4)
patt = epm.GenerateString(4, 4)

print 
print "Random text (5000), random pattern (4). Alphabet 4."
print "-"*30

print "Border Array", epm.borderSearch(stri, patt)
print "KMP", epm.kmpSearch(stri, patt)
print "Naive", epm.naiveSearch(stri, patt)
print "BWT", bwt.bwt_search(stri, patt)


stri = epm.GenerateString(30, 1)
patt = epm.GenerateString(4, 1)

print 
print "All match (30), pattern (4). Alphabet 1."
print "-"*30

print "Border Array", epm.borderSearch(stri, patt)
print "KMP", epm.kmpSearch(stri, patt)
print "Naive", epm.naiveSearch(stri, patt)
print "BWT", bwt.bwt_search(stri, patt)


stri = epm.GenerateString(30, 1)
patt = epm.GenerateString(4, 1, 1)

print 
print "No match (50), pattern (4). Alphabet 1 (2)."
print "-"*30

print "Border Array", epm.borderSearch(stri, patt)
print "KMP", epm.kmpSearch(stri, patt)
print "Naive", epm.naiveSearch(stri, patt)
print "BWT", "Breaks"


## Naive running time:

nr = []
na = []
nn = []

for n in range(10, 50000, 50):
    stri = epm.GenerateString(n, 2)
    patt = epm.GenerateString(6, 2)
    nr.append([n, timeIt("epm.naiveSearch(stri, patt)", 0, False)])

    stri = epm.GenerateString(n, 1)
    patt = epm.GenerateString(6, 1)
    na.append([n, timeIt("epm.naiveSearch(stri, patt)", 0, False)])

    stri = epm.GenerateString(n, 1)
    patt = epm.GenerateString(6, 1, 1)
    nn.append([n, timeIt("epm.naiveSearch(stri, patt)", 0, False)])

nx = [x for [x, y] in nr]
nry = [y for [x, y] in nr]
nay = [y for [x, y] in na]
nny = [y for [x, y] in nn]

plt.plot(nx, nry, label="Random")
plt.plot(nx, nay, label="All")
plt.plot(nx, nny, label="None")
plt.savefig('Naive.png', bbox_inches='tight')

nry = [y/(x+6) for [x, y] in nr]
nay = [y/(x+6) for [x, y] in na]
nny = [y/(x+6) for [x, y] in nn]

plt.figure()
plt.plot(nx, nry, label="Random")
plt.plot(nx, nay, label="All")
plt.plot(nx, nny, label="None")
plt.savefig('NaiveS.png', bbox_inches='tight')
