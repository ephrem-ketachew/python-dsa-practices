class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    
    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True
        
        current = self.root
        while current:
            if current.value == new_node.value:
                return False
            
            if new_node.value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
                
    def contains(self, value):        
        # if self.root is None:
        #     return False
        
        # current = self.root
        # while True:
        #     if current.value == value:
        #         return True
            
        #     if value < current.value:
        #         if current.left is None:
        #             return False
        #         current = current.left
        #     else:
        #         if current.right is None:
        #             return False
        #         current = current.right
        
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
            
        return False