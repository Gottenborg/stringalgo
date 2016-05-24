
#exact pattern matching
import sys
import os
def naive(x,p):
    results = []
    for i in xrange(len(x)-len(p)+1):
        if x[i:i+len(p)] == p:
            results.append(i)
    return results

def BA(x,p):
    results = []
    s = p + "$" + x
    m = len(p)
    beta = [0] * len(s)
    for i in xrange(1,len(s) - 1):
        b = beta[i]
        while b > 0 and s[i + 1] != s[b]:
            b = beta[b-1]
        if s[i + 1] == s[b]:
            beta[i + 1] = b + 1
        else:
            beta[i + 1] = 0
    for i in xrange(len(beta)):
        if beta[i] == m:
            results.append(i-m+1-(m+1))
    return results
    
def match(i,j,m,x,p):
    while x[i] == p[j] and j <= m:
        i += 1
        j += 1
    return (i,j)
    
def KMP(x,p):
    results = []
    p = "$" + p
    m = len(p)
    beta = [0] * len(p)
    for i in xrange(1,len(p) - 1):
        b = beta[i]
        while b > 0 and p[i + 1] != p[b+1]:
            b = beta[b]
        if p[i + 1] == p[b+1]:
            beta[i + 1] = b + 1
        else:
            beta[i + 1] = 0
    beta = beta[1:]
    p = p[1:]
    m = len(p)
    beta_mark = [0] * (m+1)
    for j in xrange(1,m+1):
        beta_mark[j] = beta[j-1] + 1
    i = 0
    j = 0
    #print beta_mark
    while i <= len(x)-m+j:
        i,j = match(i,j,m,x,p)
        if j == m + 1:
            results.append(i-m)
        if j == 0:
            i += 1
        else:
            j = beta_mark[j]      
    return results
    
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
    
def simple_string(n, step):
    simpleList = []
    for i in xrange(0,n+1, step):
        simpleList.append("b"*i)
    return simpleList

def stringreader(filename):
    with open(filename) as f:
        string = f.read()
    return string

class Node:
    def __init__(self, label, left=None, right=None, parent = None):
        self.label = label
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        output = "Node with label: %r \n" % (self.label,)
        if self.left==None:
            output += "No child | "
        else:
            output += "Child with label: %r | " % (self.left.label,)
        if self.right==None:
            output += "No sibling | "
        else:
            output += "Sibling with label: %r | " % (self.right.label,)
        if self.parent== None:
            output += "no parent "
        else:
            output+= "parent with label: %r" % (self.parent.label)
        return output

class SuffixTree(object):

    def __init__(self, string):
        self.string = string+"$"
        self.root = Node(None)
        self.construct()

    def __len__(self):
        return len(self.string)

    def __str__(self):
        output = "\t Suffix Tree of " + self.string[:-1] + "\n"

        return output

    def construct(self):

        n = len(self.string)

        for i in range(0, n):
            self.add(i, n-1)
        self.fix_parents(self.root)
    ## Find the correct position to add the ending.
    def add(self, i, n):

        node = self.root

        if node.left==None:
            node.left = Node(self.storeInts(i, n), parent = node)
        else:
            self.add_recrusion(node.left, i, n)

    ## Recrusive add
    def add_recrusion(self, node, i, n):

        k = self.match(self.getInts(node.label), (i, n))

        if k==-1:
            if node.right==None:
                node.right = Node(self.storeInts(i, n), parent = node.parent)

            else:
                self.add_recrusion(node.right, i, n)
        else:
            label = self.getInts(node.label)
            if k>=label[1]:
                self.add_recrusion(node.left, i+(label[1]-label[0])+1, n)
            else:
                self.correct(node, k, i, n)

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

    def correct(self, node, k, i, n):

        if node.left==None:
            j, n = self.getInts(node.label)
            node.label = self.storeInts(j, k-1)
            if node.right != None:
                node.right.parent = node.parent
            node.left = Node(self.storeInts(k, n), None, Node(self.storeInts(i+(k-j), n),parent = node), parent = node)

        else:
            j, m = self.getInts(node.label)
            node.label = self.storeInts(j, k-1)
            node.left.parent = node
            if node.right != None:
                node.right.parent = node.parent
            node.left = Node(self.storeInts(k, m), node.left, Node(self.storeInts(i+(k-j), n),parent = node), parent = node)


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

    def length_of_node(self, node, length_list, length = 0):
        if node != None and node.label != None:
            ints = self.getInts(node.label)
            length = length + (ints[1] - ints[0])+1
            if node.parent != None:
                self.length_of_node(node.parent, length_list, length)
        if node.parent == None:
            if node.label == None:
                length_list.append(length)
                return length

            ints = self.getInts(node.label)
            length = length + (ints[1] - ints[0])
            length_list.append(length)
            return length

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
        length_list = []
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
                for k in xrange(len(matches)):
                    #Get the length of the suffixes ending in the leaves
                    self.length_of_node(matches[k], length_list)
                    matches[k] = self.getInts(matches[k].label)
                    match_indexes.append(len(self.string) - length_list[k])
                if len(matches) == 0:
                    matches.append(current_node)
                    self.length_of_node(matches[0], length_list)
                    match_indexes.append(len(self.string) - length_list[0])
                    matches[0] = self.getInts(current_node.label)

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


def timeItonce(code):
    from time import time
    st = time()
    exec code
    thetime = time()-st
    #print("----- It took %.5f seconds to run: %s with %d iterations -----" % (thetime, code, 10**0))
    return thetime
    
if __name__ == "__main__":
    #x = stringreader("chr1_10000000.txt")
    #teststrings = []
    #naive_results = []
    #BA_results = []
    #KMP_results = []
    #n = []
    #for fn in os.listdir('test'):
    #    if os.path.isfile(fn):
    #        teststrings.append(stringreader(fn))
    import matplotlib.pyplot as plt
    
    #for p in teststrings:
    #    print len(p)
    #    n.append(len(p))
    #    naive_results.append(timeItonce("naive(x,p)"))
    #    BA_results.append(timeItonce("BA(x,p)"))
    #    KMP_results.append(timeItonce("kmpSearch(x,p)"))
        
    #plt.scatter(n,BA_results, color = ["blue"])
    #plt.scatter(n, KMP_results, color = ["yellow"])
    #plt.show()
    
    #plt.scatter(n,BA_results, color = ["blue"], label = "BA search")
    #plt.scatter(n, KMP_results, color = ["yellow"], label = "KMP search")
    #plt.scatter(n,naive_results, color = ["red"], label = "Naive search")
    #plt.legend(loc = "upper left")
    #plt.show()
    x = stringreader("walrus-and-carpenter.txt")
    stree = SuffixTree(x)
    import random
    distr = [x.split(" ")[10]]
    distr.append(distr[0][0:4])
    distr.append(" ### ")
    #distr += len(distr)/2 * ["#"]
    count = [0]
    suffixTime = timeItonce("SuffixTree(x)")
    timeSuffix = [suffixTime]
    timeNaive = [0]
    timeBA = [0]
    timeKMP = [0]
    for i in xrange(1,100000):
        word = random.sample(distr, 1)[0]
        count.append(count[i-1] + 1)
        timeSuffix.append(timeSuffix[i-1] + timeItonce("stree.search(word)"))
        timeNaive.append(timeNaive[i-1] + timeItonce("naive(x,word)"))
        timeBA.append(timeBA[i-1] + timeItonce("BA(x,word)"))
        timeKMP.append(timeKMP[i-1] + timeItonce("kmpSearch(x,word)"))

    plt.scatter(count, timeSuffix, color = ["red"], label = 'Suffix search')
    plt.scatter(count, timeNaive, color = ["yellow"], label = 'Naive search')
    plt.scatter(count, timeBA, color = ["blue"], label = 'BA search')
    plt.scatter(count, timeKMP, color = ["green"], label = 'KMP search')
    plt.ylabel('Running time (seconds)', fontsize = 18)
    plt.xlabel('N', fontsize = 22)
    plt.legend(loc = 'upper left')
    plt.show()
    plt.scatter(count[0:15000], timeSuffix[0:15000], color = ["red"], label = 'Suffix search')
    plt.scatter(count[0:15000], timeNaive[0:15000], color = ["yellow"], label = 'Naive search')
    plt.scatter(count[0:15000], timeBA[0:15000], color = ["blue"], label = 'BA search')
    plt.scatter(count[0:15000], timeKMP[0:15000], color = ["green"], label = 'KMP search')
    plt.ylabel('Running time (seconds)', fontsize = 18)
    plt.xlabel('Number of searches', fontsize = 18)
    plt.legend(loc = 'upper left')
    plt.show()



    
