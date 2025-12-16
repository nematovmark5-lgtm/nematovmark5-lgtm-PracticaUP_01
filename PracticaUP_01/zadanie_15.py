class MinBinaryHeap:
    def __init__(self):
        self.heap_array = []
    
    def parent_index(self, i):
        return (i - 1) // 2
    
    def left_child_index(self, i):
        return 2 * i + 1
    
    def right_child_index(self, i):
        return 2 * i + 2
    
    def swap_elements(self, i, j):
        self.heap_array[i], self.heap_array[j] = self.heap_array[j], self.heap_array[i]
    
    def sift_up(self, i):
        while i > 0 and self.heap_array[self.parent_index(i)] > self.heap_array[i]:
            self.swap_elements(i, self.parent_index(i))
            i = self.parent_index(i)
    
    def sift_down(self, i):
        smallest = i
        left = self.left_child_index(i)
        right = self.right_child_index(i)
        n = len(self.heap_array)
        
        if left < n and self.heap_array[left] < self.heap_array[smallest]:
            smallest = left
        
        if right < n and self.heap_array[right] < self.heap_array[smallest]:
            smallest = right
        
        if smallest != i:
            self.swap_elements(i, smallest)
            self.sift_down(smallest)
    
    def insert_value(self, value):
        self.heap_array.append(value)
        self.sift_up(len(self.heap_array) - 1)
    
    def extract_minimum(self):
        if len(self.heap_array) == 0:
            raise IndexError("Куча пуста")
        
        if len(self.heap_array) == 1:
            return self.heap_array.pop()
        
        min_value = self.heap_array[0]
        self.heap_array[0] = self.heap_array.pop()
        self.sift_down(0)
        
        return min_value
    
    def get_minimum(self):
        if len(self.heap_array) == 0:
            raise IndexError("Куча пуста")
        return self.heap_array[0]
    
    def build_from_array(self, arr):
        self.heap_array = arr[:]
        n = len(self.heap_array)
        
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(i)
    
    def is_valid_heap(self):
        n = len(self.heap_array)
        
        for i in range(n):
            left = self.left_child_index(i)
            right = self.right_child_index(i)
            
            if left < n and self.heap_array[left] < self.heap_array[i]:
                return False
            
            if right < n and self.heap_array[right] < self.heap_array[i]:
                return False
        
        return True
    
    def size(self):
        return len(self.heap_array)
    
    def is_empty(self):
        return len(self.heap_array) == 0
    
    def display_heap(self):
        print("Бинарная мин-куча:")
        
        if self.is_empty():
            print("Пустая")
            return
        
        height = 0
        n = len(self.heap_array)
        while (1 << height) - 1 < n:
            height += 1
        
        level = 0
        idx = 0
        
        while level < height:
            elements = min(1 << level, n - idx)
            spaces = (1 << (height - level)) - 1
            
            print(" " * spaces, end="")
            
            for i in range(elements):
                print(f"{self.heap_array[idx]:2}", end="")
                idx += 1
                
                if i < elements - 1:
                    print(" " * (2 * spaces + 1), end="")
            
            print()
            level += 1
