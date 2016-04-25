class Node:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __str__(self):
        output = "Node with label: %r \n" % (self.label,)
        if self.left==None:
            output += "No child | "
        else:
            output += "Child with label: %r | " % (self.left.label,)
        if self.right==None:
            output += "No sibling "
        else:
            output += "Sibling with label: %r" % (self.right.label,)
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

    ## Find the correct position to add the ending.
    def add(self, i, n):

        node = self.root

        if node.left==None:
            node.left = Node((i, n))
        else:
            self.add_recrusion(node.left, i, n)

    ## Recrusive add
    def add_recrusion(self, node, i, n):

        k = self.match(node.label, (i, n))

        if k==-1:
            if node.right==None:
                node.right = Node((i, n))
            else:
                self.add_recrusion(node.right, i, n)
        else:
            if k>=node.label[1]:
                self.add_recrusion(node.left, i+(node.label[1]-node.label[0])+1, n)
            else:
                self.correct(node, k, i, n)

    # Find where they match or miss match.
    def match(self, pair1, pair2):

        if self.string[pair1[0]]!=self.string[pair2[0]]:
            return -1

        for i, j in zip(range(pair1[0], pair2[1]+1),range(pair2[0], pair2[1]+1)):
            if self.string[i]!=self.string[j]:
                return i
        return pair1[1]

    def correct(self, node, k, i, n):

        if node.left==None:
            j, n = node.label
            node.label = (j, k-1)
            node.left = Node((k, n), None, Node((i+(k-j), n)))
        else:
            j, m = node.label
            node.label = (j, k-1)
            node.left = Node((k, m), node.left, Node((i+(k-j), n)))
    
    def search(self, term):
        pass

stree = SuffixTree("Mississippi")


# print
# print "First level"
# print stree.root
# print stree.root.left
# print stree.root.left.right
# print stree.root.left.right.right
# print stree.root.left.right.right.right
# print stree.root.left.right.right.right.right

# print
# print "Branches of 'M'"
# print stree.root
# print stree.root.left

# print
# print "Branches of 'i'"
# print stree.root
# print stree.root.left
# print stree.root.left.right
# print stree.root.left.right.left
# print stree.root.left.right.left.right
# print stree.root.left.right.left.left
# print stree.root.left.right.left.left.right
# print stree.root.left.right.left.left.left

# print
# print "Branches of 's'"
# print stree.root
# print stree.root.left
# print stree.root.left.right
# print stree.root.left.right.right
# print stree.root.left.right.right.left
# print stree.root.left.right.right.left.right
# print stree.root.left.right.right.left.right.left

# print
# print "Branches of 'p'"
# print stree.root
# print stree.root.left
# print stree.root.left.right
# print stree.root.left.right.right.right
# print stree.root.left.right.right.right.left
# print stree.root.left.right.right.right.left.right


def scanallnodes(node):
    if node==None: return None
    print node
    scanallnodes(node.left)
    scanallnodes(node.right)

scanallnodes(stree.root)

print
#print stree.search("ss")


from sys import getsizeof

print "Object itself:", getsizeof(stree)
print "Root:", getsizeof(stree.root)
print "Root label:", getsizeof(stree.root.label)
print "Root child:", getsizeof(stree.root.left)
print "First child label:", getsizeof(stree.root.left.label)

def getTotalMemory(ST):
    
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

def find_leaves(node, leaf_list):

    if node != None:
        if node.left == None:
            leaf_list.append(node.label)
        find_leaves(node.left, leaf_list)
        find_leaves(node.right, leaf_list)

print "Total memory usage of Mississippi: ", getTotalMemory(stree)

stree = SuffixTree("Banana")

print "Total memory usage of Banana: ", getTotalMemory(stree)

timeIt("SuffixTree('Mississippi')", 3)
timeIt("SuffixTree('Banana')", 3)

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

    ## Find the correct position to add the ending.
    def add(self, i, n):

        node = self.root

        if node.left==None:
            node.left = Node(self.storeInts(i, n))
        else:
            self.add_recrusion(node.left, i, n)

    ## Recrusive add
    def add_recrusion(self, node, i, n):

        k = self.match(self.getInts(node.label), (i, n))

        if k==-1:
            if node.right==None:
                node.right = Node(self.storeInts(i, n))
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
            node.left = Node(self.storeInts(k, n), None, Node(self.storeInts(i+(k-j), n)))
        else:
            j, m = self.getInts(node.label)
            node.label = self.storeInts(j, k-1)
            node.left = Node(self.storeInts(k, m), node.left, Node(self.storeInts(i+(k-j), n)))

    def storeInts(self, int1, int2):
        return int1+int2*1000000
    
    def getInts(self, value):
        int2 = value/1000000
        return value-int2*1000000, int2


    def search(self, term):

        current_node = self.root.left
        matches = []
        i = 0
        j = 0
        while current_node.label != None and current_node.left != None or current_node.right != None:

            ints = self.getInts(current_node.label)
            string = self.string[ints[0]:ints[1]+1]
            print "current node:"
            print string

            #While no mismatch in the current node is found continue through the node
            while i < len(term) and i-j < len(string) and term[i] == string[i-j]:
                i += 1
                print i

            #if the search term is depleted
            if i == len(term):
                #find all leaf nodes from this node
                find_leaves(current_node.left, matches)
                for k in xrange(len(matches)):
                    matches[k] = self.getInts(matches[k])
                if len(matches) == 0:
                    matches.append(self.getInts(current_node.label))
                return matches

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


print
print "Storing 2 ints in one int, versus a tuple of 2 ints"
    
stree1 = SuffixTree("Mississippi")
                                        
print "Total memory usage of Mississippi: ", getTotalMemory(stree1)

stree2 = SuffixTree("Banana")

print "Total memory usage of Banana: ", getTotalMemory(stree2)

timeIt("SuffixTree('Mississippi')", 3)
timeIt("SuffixTree('Banana')", 3)
