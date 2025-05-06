class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        current = self.first
        while current:
            print(current.value, end=' ')
            current = current.next
            
            
    def enqueue(self, value):
        new_node = Node(value)
        self.length += 1
        if self.first is None:
            self.first = new_node
            self.last = new_node
            return True
        self.last.next = new_node
        self.last = new_node
        return False
    
    def dequeue(self):
        if self.first is None:
            return None
        self.length -= 1
        temp = self.first
        if self.first.next is None:
            self.first =  self.last = None
            return temp
        self.head = self.head.next
        temp.next = None
        return temp