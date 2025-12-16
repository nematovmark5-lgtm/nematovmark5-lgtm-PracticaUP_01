class ArrayFixed:
    def __init__(self, max_elements):
        self.limit = max_elements
        self.count = 0
        self.container = [None] * max_elements
    
    def add_back(self, value):
        if self.count >= self.limit:
            raise BufferError("Достигнут максимум массива")
        self.container[self.count] = value
        self.count += 1
    
    def add_front(self, value):
        if self.count >= self.limit:
            raise BufferError("Достигнут максимум массива")
        for pos in range(self.count, 0, -1):
            self.container[pos] = self.container[pos-1]
        self.container[0] = value
        self.count += 1
    
    def insert_at(self, pos, value):
        if pos < 0 or pos > self.count:
            raise IndexError("Неверная позиция")
        if self.count >= self.limit:
            raise BufferError("Достигнут максимум массива")
        for i in range(self.count, pos, -1):
            self.container[i] = self.container[i-1]
        self.container[pos] = value
        self.count += 1
    
    def delete_at(self, pos):
        if pos < 0 or pos >= self.count:
            raise IndexError("Неверная позиция")
        for i in range(pos, self.count - 1):
            self.container[i] = self.container[i+1]
        self.container[self.count - 1] = None
        self.count -= 1
    
    def locate(self, value):
        for i in range(self.count):
            if self.container[i] == value:
                return i
        return -1
    
    def __str__(self):
        items = []
        for i in range(self.count):
            if self.container[i] is not None:
                items.append(str(self.container[i]))
        return f"[{', '.join(items)}]"
