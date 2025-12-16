class NodeSingle:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListSingleLinked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self, value):
        new_node = NodeSingle(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def push_back(self, value):
        new_node = NodeSingle(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def delete(self, value):
        if self.head is None:
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, value):
        current = self.head
        idx = 0
        while current is not None:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next
        return f"[{', '.join(result)}]" if result else "[]"
