class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def _left_child(self, index):
        return index * 2 + 1
    
    def _right_child(self, index):
        return index * 2 + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        parent_index = self._parent(current_index)
        
        while parent_index >= 0 and self.heap[current_index] > self.heap[parent_index]:
            self._swap(current_index, parent_index)
            current_index = parent_index
            parent_index = self._parent(current_index)
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            self._swap(0, len(self.heap) - 1)
            removed_item = self.heap.pop()
            parent_index = 0
            
            while parent_index < len(self.heap):
                if self._left_child(parent_index) >= len(self.heap):
                    return removed_item
                
                if self._right_child(parent_index) >= len(self.heap) or self.heap[self._left_child(parent_index)] >= self.heap[self._right_child(parent_index)]:
                    if self.heap[parent_index] > self.heap[self._left_child(parent_index)]:
                        return removed_item
                    self._swap(parent_index, self._left_child(parent_index))
                    parent_index = self._left_child(parent_index)
                else:
                    if self.heap[parent_index] > self.heap[self._right_child(parent_index)]:
                        return removed_item
                    self._swap(parent_index, self._right_child(parent_index))
                    parent_index = self._right_child(parent_index)
            
# heap = MaxHeap()
# heap.insert(99)
# heap.insert(78)
# heap.insert(56)
# heap.insert(64)
# heap.insert(58)
# heap.insert(31)
# heap.insert(27)
# heap.insert(53)
# heap.insert(100)
# heap.insert(79)

# print(heap.heap)
# heap.remove()
# print(heap.heap)

# for val in [50, 30, 40, 10, 5, 20, 35]:
#     heap.insert(val)

# print(heap.heap)
# heap.remove()
# print(heap.heap)