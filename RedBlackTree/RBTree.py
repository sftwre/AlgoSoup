
from Node import *
from Colors import Color

'''
Red black tree that stores nodes, performs rotations,
and stores a pointer to the root of the tree

Isaac Buitrago
'''
class RBTree:

    '''
        Purpose:
            Constructor for Graph
    '''
    def __init__(self):

        self.nil = None

        self.root = self.nil

    '''

        Purpose:
          Creates a new node and inserts it into a proper location in the tree

        Parameters:
            key - value of new node to insert in the tree
        Notes:
            Calls insertFixup to maintain the properties of a Red-Black tree

    '''
    def insert(self, key):

        y = self.nil

        x = self.root

        # create the new node
        z = Node(key, Color.RED)

        while x != self.nil:

            y = x

            if z.key < x.key:

                x = x.left

            elif z.key > x.key:

                x = x.right

        # set the parent of the new node
        z.parent = y

        # inserted into empty Tree
        if y == self.nil:

            self.root = z

        elif z.key < y.key:

            y.left = z

        else:
            y.right = z

        self.insertFixup(z)

    '''
        Purpose:
           Reorders nodes in the tree after insertion

        Parameters:
            node - newly inserted node in tree

        Notes:
            Performs re-coloring if uncle and parent of node is red
            Performs right rotation and left rotation if the new
            node is in a zig zag location from grandparent
    '''
    def insertFixup(self, node):

        # while the parent is red, their may be an imbalance
        while node.parent != self.nil and node.parent.color == Color.RED:

            # on left branch of grandparent
            if node.parent == node.parent.parent.left:

                y = node.parent.parent.right

                # case 1, recolor parent and uncle
                if y != self.nil and y.color == Color.RED:

                    y.color = node.parent.color = Color.BLACK

                    node.parent.parent.color = Color.RED

                    node = node.parent.parent

                else:

                    # case 2, perform left rotation
                    if node == node.parent.right:

                        node = node.parent

                        self.leftRotate(node)

                    # case 3, perform right rotation and recolor nodes
                    node.parent.color = Color.BLACK

                    node.parent.parent.color = Color.RED

                    self.rightRotate(node.parent.parent)

            # on the right branch of grandparent
            else:

                y = node.parent.parent.left

                # case 1, recolor parent and uncle
                if y != self.nil and y.color == Color.RED:

                    y.color = node.parent.color = Color.BLACK

                    node.parent.parent.color = Color.RED

                    node = node.parent.parent

                else:

                    # case 2, perform right rotation
                    if node == node.parent.left:

                        node = node.parent

                        self.rightRotate(node)

                    # case 3, perform left rotation and recolor nodes
                    node.parent.color = Color.BLACK

                    node.parent.parent.color = Color.RED

                    self.leftRotate(node.parent.parent)

        self.root.color = Color.BLACK

    '''
        Purpose:
            Rotates the node to the left of it's children nodes

        Parameters:
            nodes - node to initiate rotation
            
        Notes:
            Adjusts parent, left, and right references as needed
    '''
    def leftRotate(self, node):

        y = node.right

        # set node's new right child
        node.right = y.left

        if y.left != self.nil:

            y.left.parent = node

        # set parent of y
        y.parent = node.parent

        if node.parent == self.nil:

            self.root = y

        elif node == node.parent.left:

            node.parent.left = y

        else:
            node.parent.right = y

        y.left = node

        node.parent = y

    '''
        Purpose:
            Rotates the node to the right of it's children nodes

        Parameters:
            nodes - node to initiate rotation
            
        Notes:
            Adjusts parent, left, and right references as needed
       '''
    def rightRotate(self, node):

        # right child of node
        x = node.left

        # set right child of x to be left of node
        node.left = x.right

        # set parent of new child
        x.right.parent = node

        # set parent of x
        x.parent = node.parent

        # new root
        if node.parent == self.nil:

            self.root = x

        elif node == node.parent.right:

            node.parent.left = x

        else:
            node.parent.right = x


        x.right = node

        node.parent = x

    '''
        Purpose
            Removes the reference counts for each node
            so Garbage collection can dispose of un-referenced nodes.
            
        Parameters:
            node - reference to node in RBTree
            
        Notes:
            Uses a post-order traversal to remove references
    '''
    def clear(self, node):

        if node == self.nil:
            return

        self.clear(node.left)

        self.clear(node.right)

        node.left = None
        node.right = None

        if node.parent != None:
            node.parent = None

        # root node reached
        else:
            self.root = None








