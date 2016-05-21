import sys
import heapq

class Node:
    def __init__(self, label, left=None, right=None, parent = None, index = None, dr = None):
        self.label = label
        self.left = left
        self.right = right
        self.parent = parent
        self.index = index
        self.dr = dr

    def __str__(self):
        output = "Node with label: %r \n" % (self.label)
        if self.left==None:
            output += "No child | "
        else:
            output += "Child with label: %r | " % (self.left.label)
        if self.right==None:
            output += "No sibling | "
        else:
            output += "Sibling with label: %r | " % (self.right.label)
        if self.parent== None:
            output += "no parent "
        else:
            output+= "parent with label: %r | " % (self.parent.label)
        output += "index: %r | " % (self.index)
        output += "depth range: %r " % (self.dr, )
        return output

class SuffixTree(object):

    def __init__(self, string):
        self.string = string+"$"
        self.root = Node(None)
        self.construct()
        self.table = [0]*len(self.string)
        self.rtable = [0]*len(self.string)

    def __len__(self):
        return len(self.string)

    def __str__(self):
        output = "\t Suffix Tree of " + self.string[:-1] + "\n"

        return output

    def construct(self):

        n = len(self.string)

        c = 0

        for i in range(0, n):
            self.add(i, n-1, c)
            c += 1
        self.fix_parents(self.root)

    ## Find the correct position to add the ending.
    def add(self, i, n, c):

        node = self.root

        if node.left==None:
            node.left = Node(self.storeInts(i, n), parent = node, index = c)
        else:
            self.add_recrusion(node.left, i, n, c)

    ## Recrusive add
    def add_recrusion(self, node, i, n, c):

        k = self.match(self.getInts(node.label), (i, n))

        if k==-1:
            if node.right==None:
                node.right = Node(self.storeInts(i, n), parent = node.parent, index=c)
            else:
                self.add_recrusion(node.right, i, n, c)
        else:
            label = self.getInts(node.label)
            if k>=label[1]:
                self.add_recrusion(node.left, i+(label[1]-label[0])+1, n, c)
            else:
                self.correct(node, k, i, n, c)

    # Find where they match or miss match.
    def match(self, pair1, pair2):

        if pair1[0]>=len(self.string): pair1 = (len(self.string)-1, pair1[1])
        if pair2[0]>=len(self.string): pair2 = (len(self.string)-1, pair2[1])
        if self.string[pair1[0]]!=self.string[pair2[0]]:
            return -1

        for i, j in zip(range(pair1[0], pair2[1]+1),range(pair2[0], pair2[1]+1)):
            if self.string[i]!=self.string[j]:
                return i
        return pair1[1]

    def correct(self, node, k, i, n, c):

        if node.left==None:
            j, m = self.getInts(node.label)
            node.label = self.storeInts(j, k-1)
            if node.right != None:
                node.right.parent = node.parent
            node.left = Node(self.storeInts(k, m), None, Node(self.storeInts(i+(k-j), n), parent = node, index = c), parent = node, index = node.index)
            node.index = None

        else:
            j, m = self.getInts(node.label)
            node.label = self.storeInts(j, k-1)
            node.left.parent = node
            if node.right != None:
                node.right.parent = node.parent
            node.left = Node(self.storeInts(k, m), node.left, Node(self.storeInts(i+(k-j), n), parent = node, index = c), parent = node, index = node.index)
            node.index = None

    def storeInts(self, int1, int2):
        return int1+int2*1000000

    def getInts(self, value):
        int2 = value/1000000
        return value-int2*1000000, int2

    def find_leaves(self, node, leaf_list):

        if node != None:
            if node.left == None:
                leaf_list.append(node)
            self.find_leaves(node.left, leaf_list)
            self.find_leaves(node.right, leaf_list)

    def fix_parents(self, node):
        if node != None and node.left != None:
            node.left.parent = node
            self.fix_parents(node.left)
        if node.right != None:
            node.right.parent = node.parent
            self.fix_parents(node.right)

    def search(self, term):
        current_node = self.root.left
        matches = []
        match_indexes = []
        i = 0
        j = 0
        while current_node.label != None:

            ints = self.getInts(current_node.label)
            string = self.string[ints[0]:ints[1]+1]

            #While no mismatch in the current node is found continue through the node
            while i < len(term) and i-j < len(string) and term[i] == string[i-j]:
                i += 1

            #if the search term is depleted
            if i == len(term):
                #find all leaf nodes from this node
                self.find_leaves(current_node.left, matches)
                if len(matches) == 0:
                    match_indexes = current_node.index
                for k in matches:
                    match_indexes.append(k.index)

                return match_indexes

            #if the label is depleted
            if i-j == len(string):
                j = i

                #if the current label has a child, go to that child. Else, we are done and the search term was not found
                if current_node.left != None:
                    current_node = current_node.left
                    continue
                else:
                    return None

            #if a mismatch is found go to a sibling and try there, if no sibling: Search term is not in the tree
            if term[i] != string[i-j]:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    return None

    def length_of_node(self, node, length = 0):
        if node != None and node.label != None:
            ints = self.getInts(node.label)
            length = length + (ints[1] - ints[0])+1
            if node.parent != None:
                self.length_of_node(node.parent, length)
        if node.parent == None:
            if node.label == None:
                return length

            ints = self.getInts(node.label)
            length = length + (ints[1] - ints[0])
            return length

    def dfs(self, node, table, s, i):
        if node.left == None:
            table[i] = node.index
            i += 1

        if node.left != None:
            ns, i = self.dfs(node.left, table, s, i)
            node.dr = self.storeInts(s, i)

        if node.right != None:
            s, i = self.dfs(node.right, table, i, i)

        return s, i

    def getLL(self, dr):
        return self.table[dr[0]:dr[1]]

    def collectLLs(self, node, LL):

        LLs = []
        node = node.left

        # Traverse the siblings
        while node!=None:
            # Check whether the node has range
            if node.dr!=None:
                # Collect the leaf list
                l, r = self.getInts(node.dr)
                LLs.append((self.getLL((l, r)), (l, r)))
            else:
                # If leaf append index instead.
                if node.index in LL:
                    LLs.append(([node.index], (node.index, node.index)))
            node = node.right

        return sorted(LLs, key = lambda x: len(x[0]), reverse=True)

    def crawl(self, node, bp, S, oD):

        # If reached None for some reason, then stop.
        if node==None: return 0

        # If the node as no child, then it is a leaf, and should not be run.
        if node.left==None:
            # Checking whether there is a sibling (might not be a leaf)
            if node.right!=None:
                self.crawl(node.right, bp, S, oD)
                return 0
            else: return 0

        # Calculating a new leaf distance
        l, r = self.getInts(node.label)
        D = r-l+oD+1
        # Collecting the Leaf lists
        LL = self.getLL(self.getInts(node.dr))
        LLs = self.collectLLs(node, LL) # First element is large and the remaining is small (LL'(v))

        # Assigning
        largel, larger = LLs[0][1]
        small = [i[0] for i in LLs[1:]]

        ld, rd = self.getInts(node.dr)

        # Looping through the entries in small
        for j in small:
            for i in j:
                # Test 1
                if self.rtable[i+D] >= ld and self.rtable[i+D] <= rd:
                    if S[i]!=S[i+2*D]:
                        bp.add((i, D))
                #Test 2
                if self.rtable[i-D] >= largel and self.rtable[i-D] <= larger:
                    if S[i-D]!=S[i+D]:
                        bp.add((i-D, D))

        # Traverse first to a child then to a sibling.
        self.crawl(node.left, bp, S, D)
        self.crawl(node.right, bp, S, oD)


    def find_tandem_repeats(self, printing=True, output=False):
        # Annotate the tree with depth first
        self.dfs(self.root, self.table, 0, 0)
        for x in xrange(len(self.table)):
            self.rtable[self.table[x]] = x
        bp = set()
        S = self.string

        node = self.root.left

        # Initilize the algorithm
        self.crawl(node, bp, S, 0)

        if printing==True: bp = sorted(list(bp), key = lambda x: x[0])

        ln = 0

        if printing==True: points = []

        # Find all non-branching points
        for b, l in bp:
            ln += self.left_rotate(b, l, 2)
            nb = self.left_rotate(b, l, 2)
            if printing==True: points.append(((b, l, 2), "branching"))
            if printing==True:
                for i in xrange(1, nb+1):
                    points.append(((b-i, l, 2), "non-branching"))

        if printing==True: points = sorted(points, key = lambda x: x[0][1])
        if printing==True: points = sorted(points, key = lambda x: x[0][0])

        if printing==True:
            for i, j in points:
                print "(%i,%i,%i)" % i, j

        if printing==True: points = [("(%i,%i,%i) " % (i[0])) + i[1] for i in points]

        if printing==True and output==True: return (len(bp), ln), points

        return len(bp), ln

    # Find the number of non-branching points, for a branching point.
    def left_rotate(self, i, l, t):
        c = 0
        while i>0 and self.string[i-1]==self.string[i+(l*t)-1]:
            c += 1
            i -= 1
        return c

def scanallnodes(node):
    if node==None: return None
    print node
    scanallnodes(node.left)
    scanallnodes(node.right)

def getTotalMemory(ST):

    from sys import getsizeof

    if ST is None: return getsizeof(ST)

    if type(ST)==SuffixTree:
        totalmemory = getsizeof(ST)+getsizeof(ST.root)+getsizeof(ST.root.label)+getsizeof(ST.root.left)+getsizeof(ST.root.right)
        node = ST.root.left
    else:
        totalmemory = 0
        node = ST

    while node is not None:
        totalmemory += getsizeof(node.label)+getsizeof(node.left)+getsizeof(node.right)

        totalmemory += getTotalMemory(node.left)

        node = node.right

    return totalmemory

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

def timeItonce(code):
    from time import time
    st = time()
    exec code
    thetime = time()-st
    print("----- It took %.5f seconds to run: %s with %d iterations -----" % (thetime, code, 10**0))
    return thetime

def stringreader(filename):
    with open(filename) as f:
        string = f.read()
    return string


if __name__ == "__main__":
    file = stringreader(sys.argv[1])
    stree = SuffixTree(file)

    #print stree.search(sys.argv[2])
    thetable = [0] * len(stree.string)
    stree.dfs(stree.root, thetable, 0, 0)
    #print thetable
    count = stree.find_tandem_repeats()
    print count[0], count[1]
    #print stree.table
    #scanallnodes(stree.root)
    avgtime = timeItonce("stree.find_tandem_repeats(False)")

    #from math import log

    #iterations = (len(sys.argv[1])+1)*log((len(sys.argv[1])+1))
    #iterations2 =  (len(sys.argv[1])+1)**2

    #print "Iterations: (n log n) ", iterations
    #constant = avgtime/iterations
    #print "The constant: (n log n) ", constant
    #print "Expected time: (n log n) ", iterations*(10**-6)
    #print "Iterations: (n^2) ", iterations2
    #constant2 = avgtime/iterations2
    #print "The constant: (n^2)", constant2
    #print "Expected time: (n log n)", iterations*(10**-7)





# Quick debugging tool.
#print
#print
tests = "abaababaabaab"
sterm = 'aba'
testt = SuffixTree(tests)

# scanallnodes(testt.root)

#print
#print tests, sterm
#print testt.search(sterm)
#print testt.find_tandem_repeats()
