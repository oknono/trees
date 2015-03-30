# 1. Choose representation for Tree
# A tree consists of nodes. For this purpose a node has a name, a parent (or None if root),
# and 0..n children (if 0 then node is leaf)
# A default new node doesn't have parent or children. They can be added to an object if these nodes have
# been instantiated. In this code, the parents are instantiated first and can be added when constructing 
# a new node. The children need to be added later.

# class for a node object
class Node(object):
    """Class to create a simple node object and some methods"""
    
    # create new node object
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent = parent
        self.children = children
    
    # assume parent of a node is a node
    def add_parent(self, parent):
        """Set the parent of a node"""
        self.parent = parent
    
   
    def add_children(self, children):
        """Set the children of a node, list of node(s)"""
        self.children = children

    #def get_parent(self):
    #    """Return the parent node of a node"""
    #    return self.parent.value

    def get_parent(self):
        """Return the parent node of a node"""
        return self.parent

    #def get_children(self):
    #    """Return a list of all the values of the children nodes"""
    #    child_list = []
    #    for child in self.children:
    #        child_list.append(child.value)
    #    return child_list

    def get_children(self):
        return self.children

    def is_root(self):
        return self.parent == None

    def is_leaf(self):
        return self.children == [] 

    # print the value of the object, not object itself
    # This doesn't seem to work, fix it!
    def __repr__(self):
        return self.value

# create the small tree from example.
a = Node("a")
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", b)
g = Node("g", c)
h = Node("h", c)

# add the children to the nodes
a.add_children([b,c])
b.add_children([d,e,f])
c.add_children([g,h])

# some testing
# why does this print name of the node and not value of the node>!
print(a)
print type(a)
print a.value
print type(a.value)
print b.get_parent() == "a"
print a.is_root() == True
print b.is_root() == False
print b.is_leaf() == False
print h.is_leaf() == True
print a.get_children()

# 2. Implement DFS for tree implementation
# We are going to start the search with the root node.
# The function will check if the given node is root. 
# Besides a node, the function takes a value to check for 

# We want to start to search at the root of the tree, but with this function we could
# start with any node
def DFS(target, node):
    stack = []
    stack.append(node)
    while stack is not empty:
        visited = c_list.pop()
        if visited.value == target:
            return target
        else: 
           for child in visited. 
        


