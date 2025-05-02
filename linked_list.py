class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        current = self.head
        current_index = 0
        while current_index < index:
            current = current.next
            current_index += 1   
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        # for index in range(self.length):
        #     print(current.value, end=' ')
        #     current = current.next
        print()
            
    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1
        return True
        
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
            
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def pop(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            self.length -= 1
            node = self.head
            self.head = self.tail = None
            return node
        else:
            self.length -= 1
            current = self.head
            while current.next != self.tail:
                current = current.next
            node = self.tail
            current.next = None
            self.tail = current
            return node
            
    def pop_first(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            self.length -= 1
            node = self.head
            self.head = self.tail = None
            node.next = None
            return node
        else:
            self.length -= 1
            current = self.head
            self.head = self.head.next
            current.next = None
            return current
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index - 1)
        current = temp.next
        temp.next = current.next
        current.next = None
        self.length -= 1
        return current
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        current = self.tail
        before = None
        
        while current:
            after = current.next
            current.next = before
            before = current
            current = after
        
        # reversed_current = self.head
        # while reversed_current != self.tail:
        #     current = self.tail
        #     while current.next != reversed_current:
        #         current = current.next
        #     current.next.next = current
        #     reversed_current = current
        # self.tail.next = None
        
        # for i in range(self.length - 1):
        #     current = self.tail
        #     print(current.value)
        #     for j in range(self.length - i - 2):
        #         current = current.next
        #     print(current.value)
        #     temp = current.next
        #     temp.next = current
        # self.tail.next = None

        # current = self.head
        # if not current:
        #     return None
        # reversed_linked_list = LinkedList(current.value)
        # while current.next:
        #     current = current.next
        #     reversed_linked_list.prepend(current.value) 
        # return reversed_linked_list
    

linked_list = LinkedList(90)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.print_list()
# print(linked_list.pop())
# linked_list.print_list()
# print(linked_list.pop())
# linked_list.print_list()
# print(linked_list.pop())
# linked_list.print_list()
# print(linked_list.pop())
# linked_list.print_list()
# linked_list.append(90)
linked_list.prepend(30)
linked_list.prepend(40)
linked_list.prepend(50)
linked_list.append(70)
linked_list.append(60)
linked_list.append(20)
linked_list.print_list()

# linked_list.remove(1)
# print(linked_list.get(2).value)
# print(linked_list.set_value(2,10))
# linked_list.insert(1, 80)
# linked_list.print_list()
linked_list.reverse()
linked_list.print_list()
# print(linked_list.head.value)
# print(linked_list.tail.value)
# linked_list.pop_first()
# linked_list.pop_first()
# linked_list.pop_first()
# linked_list.print_list()
# linked_list.pop_first()
# linked_list.print_list()
# linked_list.pop_first()
# linked_list.print_list()
# linked_list.pop_first()
# linked_list.print_list()
# linked_list.pop_first()
# linked_list.print_list()
# print(linked_list.head.value)
# print(linked_list.tail.value)