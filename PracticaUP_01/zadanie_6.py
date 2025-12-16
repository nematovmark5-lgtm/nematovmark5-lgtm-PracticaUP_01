class QueueCircular:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def enqueue(self, value):
        if self.count >= self.capacity:
            self._expand()
        
        self.buffer[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
    
    def dequeue(self):
        if self.count == 0:
            raise IndexError("Очередь пуста")
        
        value = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value
    
    def front_item(self):
        if self.count == 0:
            raise IndexError("Очередь пуста")
        return self.buffer[self.front]
    
    def is_empty(self):
        return self.count == 0
    
    def _expand(self):
        new_capacity = self.capacity * 2
        new_buffer = [None] * new_capacity
        
        for i in range(self.count):
            new_buffer[i] = self.buffer[(self.front + i) % self.capacity]
        
        self.buffer = new_buffer
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.count
    
    def __str__(self):
        result = []
        for i in range(self.count):
            result.append(str(self.buffer[(self.front + i) % self.capacity]))
        return f"[{', '.join(result)}]" if result else "[]"


class QueueTwoStacks:
    def __init__(self):
        self.in_stack = StackArray()
        self.out_stack = StackArray()
    
    def enqueue(self, value):
        self.in_stack.push(value)
    
    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        
        if self.out_stack.is_empty():
            raise IndexError("Очередь пуста")
        
        return self.out_stack.pop()
    
    def front(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        
        if self.out_stack.is_empty():
            raise IndexError("Очередь пуста")
        
        return self.out_stack.peek()
    
    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()
    
    def __str__(self):
        temp = StackArray()
        result = []
        
        for i in range(self.out_stack.top_idx + 1):
            temp.push(self.out_stack.items[i])
        
        while not temp.is_empty():
            result.append(str(temp.pop()))
        
        for i in range(self.in_stack.top_idx + 1):
            result.append(str(self.in_stack.items[i]))
        
        return f"[{', '.join(result)}]" if result else "[]"
