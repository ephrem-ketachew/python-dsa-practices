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
    
    def __r_contains(self, node, value):
        if node == None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self.__r_contains(node.left, value)
        if value > node.value:
            return self.__r_contains(node.right, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, node, value):
        # if node is None:
        #     return Node(value)
        # if value < node.value:
        #     node.left = self.__r_insert(node.left, value)
        # if value > node.value:
        #     node.right = self.__r_insert(node.right, value)
        # return node
        if node.value == value:
            return False
        if value < node.value:
            if node.left is None:
                new_node = Node(value)
                node.left = new_node
                return True
            return self.__r_insert(node.left, value)
        if value > node.value:
            if node.right is None:
                new_node = Node(value)
                node.right = new_node
                return True
            return self.__r_insert(node.right, value)
    
    def r_insert(self, value):
        # self.root = self.__r_insert(self.root, value)
        if self.root is None:
            self.root = Node(value)
            return True
        return self.__r_insert(self.root, value)