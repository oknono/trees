# 1. Choose representation for Tree
# A tree consists of nodes. For this purpose a node has a name, a parent (or None if root),
# and 0..n children (if 0 then node is leaf)
# A new node doesn't have parent or children. These need to be added.

# class for a node object
class Node(object):
    # A default node has no parent and no children
    # If parent node has been instantiated we can pass this as parameter
    # We cannot pass an object that has not been created yet
    # For this we'll use add_children method
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent = parent
        self.children = children

    # seperate functions because objects need to be instantiated before the can be use in declaration
    # specify parent when creating node, children need to be added later
    def add_parent(self, parent):
        self.parent = parent

    def add_children(self, children):
        self.children = children

    def get_parent(self):
        return self.parent.value

    def get_children(self):
        # child_list = []
        # for all nodes in a tree:
        # check if self is parent
        # if parent, add to list
        # MANUAL FOR NOW
        return self.children

    def is_root(self):
        return self.parent == None

    def is_leaf(self):
        return self.children == [] 

    def __repr__(self):
        return self.value

# create the small tree from example.
# First instantiate the nodes with their parent nodes
# We don't really need children now do we?
# Can I formulate method with will deduce the children?
# That would be greaaaatttttt
a = Node("a")
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", b)
g = Node("g", c)
h = Node("h", c)

a.add_children([b,c])
b.add_children([d,e,f])
c.add_children([g,h])

print(a)
print b.get_parent()
print a.is_root()
print b.is_root()
print b.is_leaf()
print h.is_leaf()
print a.get_children()


#b = Node(a, [d, e, f])
#c = Node(a, [g, h])
#d = Node(b, [])
#e = Node(b, [])
#f = Node(b, [])
#g = Node(c, [])
#h = Node(c, [])

# 2. Implement DFS for tree implementation