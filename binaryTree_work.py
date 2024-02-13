
class Queue(objet):
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        if not self.isempty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
        
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
    
#Similar to linked list, establish the left and right child values as None
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
#Establishes the root of my tree as a Node object.      
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    #Helper function for printing traversal
    """Starts with root for traversal and an empty string, after each recursive call it will update
        to either left or right and add my "-" in between from my print function"""
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "") 
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root, "")
        else: 
            print("Traversal type" + str(traversal_type) + "is not supported.")
            return False       
    #Traverses my binary tree in pre-order    
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")   #Turns value into str for printing with "-" between nodes
            traversal = self.preorder_print(start.left, traversal)  #Recursive call down left side of tree
            traversal = self.preorder_print(start.right, traversal) #Recursive call down right side of tree
        return traversal
    
    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    def levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
# PREORDER = 1-2-4-5-3-6-7
# INORDER = 4-2-5-1-6-3-7  
# POSTORDER = 4-2-5-6-3-7-1 
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7

# Establishes my tree      
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
        
