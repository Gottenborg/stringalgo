import sys

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


def stringreader(filename):
    with open(filename) as f:
        string = f.read()
    return string


if __name__ == "__main__":
    file = stringreader(sys.argv[1])
    stree = SuffixTree(file)

    print stree.search(sys.argv[2])
