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
