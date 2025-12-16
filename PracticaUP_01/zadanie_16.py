class PriorityQueue:
    class QueueItem:
        def __init__(self, value, priority):
            self.value = value
            self.priority = priority
        
        def __lt__(self, other):
            return self.priority < other.priority
        
        def __repr__(self):
            return f"Item({self.value}, priority={self.priority})"
    
    def __init__(self):
        self.heap = MinBinaryHeap()
    
    def enqueue(self, value, priority):
        item = self.QueueItem(value, priority)
        self.heap.insert_value(item)
    
    def dequeue(self):
        if self.heap.is_empty():
            raise IndexError("Очередь пуста")
        
        item = self.heap.extract_minimum()
        return item.value, item.priority
    
    def peek(self):
        if self.heap.is_empty():
            raise IndexError("Очередь пуста")
        
        item = self.heap.get_minimum()
        return item.value, item.priority
    
    def empty(self):
        return self.heap.is_empty()
    
    def length(self):
        return self.heap.size()
    
    def schedule_tasks(self, tasks):
        results = []
        current_time = 0
        
        for task in tasks:
            self.enqueue(task['id'], task['priority'])
        
        while not self.empty():
            task_id, priority = self.dequeue()
            results.append({
                'task_id': task_id,
                'priority': priority,
                'start': current_time,
                'finish': current_time + 1
            })
            current_time += 1
        
        return results
    
    def find_k_smallest(self, array, k):
        if k <= 0 or k > len(array):
            raise ValueError("Неверное значение k")
        
        for value in array:
            self.enqueue(value, value)
        
        result = []
        for _ in range(k):
            value, _ = self.dequeue()
            result.append(value)
        
        return result
    
    def find_k_largest(self, array, k):
        if k <= 0 or k > len(array):
            raise ValueError("Неверное значение k")
        
        for value in array:
            self.enqueue(value, -value)
        
        result = []
        for _ in range(k):
            value, _ = self.dequeue()
            result.append(value)
        
        return result
    
    def merge_sorted(self, lists):
        result = []
        
        for idx, lst in enumerate(lists):
            if lst:
                self.enqueue((lst[0], idx, 0), lst[0])
        
        while not self.empty():
            value, list_idx, elem_idx = self.dequeue()[0]
            result.append(value)
            
            if elem_idx + 1 < len(lists[list_idx]):
                next_val = lists[list_idx][elem_idx + 1]
                self.enqueue((next_val, list_idx, elem_idx + 1), next_val)
        
        return result
    
    def display_queue(self):
        print("Очередь с приоритетом:")
        
        if self.heap.is_empty():
            print("Пустая")
            return
        
        temp = MinBinaryHeap()
        temp.heap_array = self.heap.heap_array[:]
        
        while not temp.is_empty():
            item = temp.extract_minimum()
            print(f"  Значение: {item.value}, Приоритет: {item.priority}")
