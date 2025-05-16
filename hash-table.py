class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for char in key:
            my_hash = (my_hash + ord(char) * 23) % len(self.data_map)
        
        return my_hash
    
    def print_hash(self):
        for i,val in enumerate(self.data_map):
            print(i, ':', val)
            
    def set_item(self, key, val):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, val])
        
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for item in self.data_map[index]:
            if item[0] == key:
                return item[1]
            
    def keys(self):
        return [item[0] for arr in self.data_map if arr is not None for item in arr]
    
    def values(self):
        return [item[1] for arr in self.data_map if arr is not None for item in arr]

# my_hash_table = HashTable()
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
# my_hash_table.print_hash()
# print(my_hash_table.get_item('nails'))

# print(my_hash_table.keys())
# print(my_hash_table.values())
