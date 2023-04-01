arr = [(1, 'apple'), (2, 'banana'), (110, 'cherry'), (123, 'date'), (132, 'elderberry'), (145, 'fig'), (154, 'grape'), (16, 'honeydew'), (173, 'imbe'), (180, 'jackfruit'), (197, 'kiwi'), (217, 'lemon'), (226, 'mango'), (235, 'nectarine'), (249, 'orange'), (253, 'pear'), (261, 'quince'), (257, 'raspberry'), (288, 'strawberry'), (329, 'tangerine')]

class hashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function_1(self, key):
        return hash(key) % self.size
    
    def hash_function_2(self, key):
        return (1+ hash(key)) % (self.size - 2)
    
    def insert(self, key, value):
        hash_key = self.hash_function_1(key)
        if self.keys[hash_key] == key:
            self.values[hash_key] = value
        elif self.keys[hash_key] is None:
            self.keys[hash_key] = key
            self.values[hash_key] = value
        else:
            step = self.hash_function_2(key)
            i = 0
            while True:
                hash_key = (hash_key + step) % self.size
                if self.keys[hash_key] == key:
                    self.values[hash_key] = value
                    break
                elif self.keys[hash_key] is None:
                    self.keys[hash_key] = key
                    self.values[hash_key] = value
                    break
                i += 1

                if i == self.size:
                    raise Exception("Hash table is full")

    


    def print_hash(self):
        t = []
        for i in range(len(self.keys)):
            t.append((self.keys[i], self.values[i]))
        print(t)



hashmap = hashTable(21)
for j,k in arr:
     hashmap.insert(j,k)
hashmap.print_hash()
