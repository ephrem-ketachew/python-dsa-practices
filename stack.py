class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        current = self.top
        while current:
            print(current.value, end=' ')
            current = current.next
            
    def push(self, value):
        new_node = Node(value)
        self.height += 1
        if self.top is None:
            self.top = new_node
            return True
        new_node.next = self.top
        self.top = new_node
        return True
    
    def pop(self):
        if self.top is None:
            return False
        self.height -= 1
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp