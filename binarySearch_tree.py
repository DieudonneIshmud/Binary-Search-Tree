"""
Decisions, decisions… Life is all about choices! 
Usually there are so many ways to go.
 An infinite expanse of roads and pathways stretches in front of you, 
 an endless gradient of details; as you consider them, your head starts to spin, your eyes start to droop, your mind races, your head pounds -
Wait a second. 
There’s no need to stress. Since we’re talking about Binary Search Trees, decisions are going to be a lot easier. 
A Binary Search Tree (BST) gives you two choices: left or right, less than or greater than, 0 or 1 — hence the name, binary.

Insering into BST: the Node will have most of the important code for the insert method
The BST class will essentially be a wrapper for the Node, hiding some of the rough edges of the internal methods to give the user a clean interface."""

class Node(object):
    def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

    def insert(self, d):
        if self.data == d: #checks if the data object already exists in the tree
            return False
            #Otherwise, it will go to the left or right depending on whether the data to insert is greater or smaller than the node’s value
        elif d < self.data:
            if self.left:
                return self.left.insert(d)
            else:
                selft.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else: # If there’s nothing on the side that is chosen, a new node is created, and we return True
                self.right = Node(d)
                return True
        #Otherwise, the method continues recursively, checking and moving left or right until the data is found or inserted in the tree.
    
                
#The BST class will wrap this neatly, beginning the recursive call on the root node like so:

class BST(object):

    def insert(self, d):
        '''Returns True if successfully inserted, false if exists'''
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True