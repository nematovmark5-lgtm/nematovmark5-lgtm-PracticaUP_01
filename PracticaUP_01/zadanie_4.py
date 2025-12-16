class NodeDouble:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class ListDoubleLinked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self, value):
        new_node = NodeDouble(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    
    def insert_after(self, node, value):
        if node is None:
            return
        
        new_node = NodeDouble(value)
        new_node.prev = node
        new_node.next = node.next
        
        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node
        
        node.next = new_node
        self.count += 1
    
    def remove_node(self, node):
        if node is None:
            return
        
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        self.count -= 1
    
    def find(self, value):
        current = self.head
        idx = 0
        while current is not None:
            if current.data == value:
                return current, idx
            current = current.next
            idx += 1
        return None, -1
    
    class Iterator:
        def __init__(self, start):
            self.current = start
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current is None:
                raise StopIteration
            data = self.current.data
            self.current = self.current.next
            return data
    
    def __iter__(self):
        return self.Iterator(self.head)
    
    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next
        return f"[{', '.join(result)}]" if result else "[]"
