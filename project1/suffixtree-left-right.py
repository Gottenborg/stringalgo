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

        print "Construction has started!"

        for i in range(0, n):
            self.add(i, n-1)

    ## Find the correct position to add the ending.
    def add(self, i, n):

        print
        print "Going to add: ", self.string[i:n+1]

        node = self.root

        print node

        if node.left==None:
            node.left = Node((i, n))
        else:
            self.add_recrusion(node.left, i, n)

    ## Recrusive add
    def add_recrusion(self, node, i, n):

        k = self.match(node.label, (i, n))

        print "-"*10
        print node
        print k

        if k==-1:
            if node.right==None:
                node.right = Node((i, n))
                print "-"*10
                print "Added:"
                print node.right
            else:
                self.add_recrusion(node.right, i, n)
        else:
            if k>=node.label[1]:
                print (i, n), (i+(node.label[1]-node.label[0])+1, n)
                self.add_recrusion(node.left, i+(node.label[1]-node.label[0])+1, n)
            else:
                self.correct(node, k, i, n)

    # Find where they match or miss match.
    def match(self, pair1, pair2):

        if self.string[pair1[0]]!=self.string[pair2[0]]:
            return -1

        for i, j in zip(range(pair1[0], pair2[1]+1),range(pair2[0], pair2[1]+1)):
            print i,j
            if self.string[i]!=self.string[j]:
                return i
        return pair1[1]

    def correct(self, node, k, i, n):

        if node.left==None:
            j, n = node.label
            node.label = (j, k-1)
            node.left = Node((k, n), None, Node((i+(k-j), n)))
            print "-"*10
            print node
            print "-"*10
            print "Added:"
            print node.left
        else:
            j, m = node.label
            node.label = (j, k-1)
            print "Note with a child being corrected"
            node.left = Node((k, m), node.left, Node((i+(k-j), n)))
            print "-"*10
            print node
            print "-"*10
            print "Added:"
            print node.left

    
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
print stree.search("ss")
