#Similar to linked list, establish the left and right child values as None
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
#Establishes the root of my tree as a Node object.      
class BinaryTree(object):
    def __innit__(self, root):
        self.root = Node(root)
        
    #Helper function for printing traversal
    """Starts with root for traversal and an empty string, after each recursive call it will update
        to either left or right and add my "-" in between from my print function"""
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "") 
        
    #Traverses my binary tree in pre-order    
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")   #Turns value into str for printing with "-" between nodes
            traversal = self.preorder_print(start.left, traversal)  #Recursive call down left side of tree
            traversal = self.preorder_print(start.right, traversal) #Recursive call down right side of tree
        return traversal
    
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
#                \
#                 8
      
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

        
