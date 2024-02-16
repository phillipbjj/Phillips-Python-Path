
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
            
    def search(self, key): #Search starts from root of the tree, calls _search() for the recursive search.
        return self._search(self.root, key) #Returns result from _search()
    
    def _search(self, node, key):
        if node is None or node.key == key: #Reached the end w/o finding the key or it was found in the current node.
            return node
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        
    def delete(self, key):
        self.root = self._delete(self.root, key) #In case the delete results in a new root
    
    def _delete(self, node, key):
          
        if node is None: #If there is no key to be deleted at that node.
            return node 
        
        if key < node.key:     
            node.left = self._delete(node.left, key)
        elif key > node.key:  
            node.right = self._delete(node.right, key)
        else:
            if node.left is None: #Checks if left child of current Node is None, so return right child
                return node.right
            elif node.right is None: #Checks if right child of current Node is None, so return left child
                return node.left
            node.key = self._min_value(node.right) #The smallest value will be the in-order successor of the current node.
            node.right = self._delete(node.right, node.key) #Needed to recursively deleted the node with the min value from the right subtree.
        return node
        
    def _min_value(self, node):
        """to find the smallest value in the right subtree, you need to iterate through the left children of the
        given node untilyou reach the leftmost (smallest) node in the subtree."""
        while node.left is not None: #Once the leftmost node is found & node.left becomes None, the loop exits.
            node = node.left      
        return node.key     #Returns leftmost node (minimum value) in the given subtree, provides the value that will replace the node after it is deleted
        
    def inorder_traversal(self):
        result = []         #Stores keys of nodes in sorted order
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]       
for node in nodes:
    bst.insert(node)    #bst is BinarySearchTree() for calling, so I can call functions within it (.insert)
        
print("Inorder traversal:", bst.inorder_traversal())      
        