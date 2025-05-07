class Stack:
    def __init__(self):
        self.stack_list = []
        
    def push(self, value):
        self.stack_list.append(value)
        return True
    
    def pop(self):
        if len(self.stack_list) == 0: 
            return None
        return self.stack_list.pop()
    
    def peek(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list[len(self.stack_list) - 1]
    
    def isEmpty(self):
        return len(self.stack_list) == 0
    

def reverse_sting(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    rev_str = ''
    while len(stack.stack_list) > 0:
        rev_str += stack.pop()
    return rev_str

def sort_stack(stack):
    sorted_stack = Stack()
    while not stack.isEmpty():
        temp = stack.pop()
        while not sorted_stack.isEmpty() and sorted_stack.peek() > temp:
            temp2 = sorted_stack.pop()
            stack.push(temp2)
        sort_stack.push(temp)
    
    while not sorted_stack.isEmpty():
        temp = stack.pop()
        stack.push(temp)