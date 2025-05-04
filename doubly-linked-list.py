class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length / 2:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        
        current = self.tail
        for _ in range(self.length - 1 - index):
            current = current.prev
        return current
    
    def set_value(self, index, value):
        node = self.get(index)
        if node is None:
            return False
        node.value = value
        return True
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:   
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        node = self.get(index - 1)
        if node is None:
            return False
        new_node = Node(value)
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        new_node.next.prev = new_node
        self.length += 1
        return True
         
    def pop(self):
        if not self.head:
            return None
        self.length -= 1
        if self.tail.prev is None:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        temp = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        temp.prev = None
        return temp
    
    def pop_first(self):
        if not self.head or self.tail.prev is None:
            return self.pop()
        self.length -= 1
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        return temp
    
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        node = self.get(index - 1)
        if node is None:
            return None
        temp = node.next
        node.next = temp.next
        temp.next.prev = node
        temp.next = None
        temp.prev = None
        temp = node.next
        self.length -= 1
        return temp
            
my_linked_list = LinkedList(2)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(9)
my_linked_list.append(1)
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.append(1)
# my_linked_list.append(0)
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()

# my_linked_list.print()
# print(my_linked_list.insert(2, 8))
# print(my_linked_list.remove(5).value)
# my_linked_list.print()