
class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    
    def _insert(self, node, key):
        #Helper insert function
        if node is None:       #If at a new node or an empty node, it will insert the provided key
            return TreeNode(key)
        
        if key < node.key:     #Recursively calls insert function on the left child of current node
            node.left = self._insert(node.left, key)
        elif key > node.key:   #Recursively calls insert function on the right child of current node
            node.right = self._insert(node.right, key)
            #Return the current node to update the tree structure at the higher levels of the recursive call stack.
        return node  
            
        
        
        
        
        
        