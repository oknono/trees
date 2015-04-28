#!/usr/bin/env python

# 1. Choose representation for Tree
# A tree consists of nodes. For this purpose a
# node has a name, a value, a parent (or None if root),
# and 0..n children (if 0 then node is leaf)
# A default new node doesn't have parent or children.
# They can be added to an object if these linked nodes have
# been instantiated. In this code, the parents are instantiated
# first and can be added as parents when constructing
# a new node. The children need to be added later.


class Node(object):
    """Class to create a simple node object and some methods"""

    def __init__(self, value, parent = None, children = []):
        """Create a new node object"""
        self._value = value
        self._parent = parent
        self._children = children

    def add_parent(self, parent):
        """Set the parent of a node - assumed this is another node"""
        self._parent = parent

    def add_children(self, children):
        """Set the children of a node, assumed this is list of node(s)"""
        self._children = children

    @property
    def value(self):
        """Return value of a node"""
        return self._value
    
    @property
    def parent(self):
        """Return the parent node of a node"""
        return self._parent
    
    @property
    def children(self):
        """Return list of child nodes"""
        return self._children

    def is_root(self):
        """Return Bool indicating if node is the root node"""
        return self._parent == None

    def is_leaf(self):
        """Return Bool indicating if note is a leaf node"""
        return self._children == []

    

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
a.add_children([b, c])
b.add_children([d, e, f])
c.add_children([g, h])

# 2. Implement DFS for tree implementation
# We are going to start the search with the root node.
# The function will check if the given node is root.
# Besides a node, the function takes a value to check for
# Note that with this function you also input other starting node

# Example run DFS("g", a)
# stack = []
# stack = [a]
# stack = [c, b]
# stack = [c, f, e, d]
# stack = [c, f, e]
# stack = [c, f]
# stack = [c]
# stack = [g]

def DFS(target, node):
    """Takes target value and start node and returns target if found in tree"""
    stack = []
    # Add root node to the stack
    stack.append(node)
    while stack != []:
        # take the last item from the list and compare
        visited = stack.pop()
        # check if this item has targer value
        if visited.value == target:
            return target
        # Add children to the list, but reverse them    
        else:
            children = visited.children
            for index in range(1, len(children) + 1):
                stack.append(children[-index])

if __name__ == '__main__':
    print DFS("d", a)
    print DFS("g", a)
    print DFS("z", a)
