class MyQueue:
    def __init__(self, value):
        self.stack1 = []
        self.stack2 = []
        
    def print(self):
        for i in range(len(self.stack1)):
            print(self.stack1[i])
            
    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(value)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            
    def dequeue(self):
        return self.stack1.pop() if self.stack1 else None