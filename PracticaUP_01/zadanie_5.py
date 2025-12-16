class StackArray:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top_idx = -1
    
    def push(self, value):
        if self.top_idx >= self.capacity - 1:
            raise OverflowError("Стек полон")
        self.top_idx += 1
        self.items[self.top_idx] = value
    
    def pop(self):
        if self.top_idx < 0:
            raise IndexError("Стек пуст")
        value = self.items[self.top_idx]
        self.items[self.top_idx] = None
        self.top_idx -= 1
        return value
    
    def peek(self):
        if self.top_idx < 0:
            raise IndexError("Стек пуст")
        return self.items[self.top_idx]
    
    def is_empty(self):
        return self.top_idx < 0
    
    def __str__(self):
        return f"[{', '.join(str(x) for x in self.items[:self.top_idx+1] if x is not None)}]"


class StackLinked:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.top_node = None
        self.size = 0
    
    def push(self, value):
        new_node = self.Node(value)
        new_node.next = self.top_node
        self.top_node = new_node
        self.size += 1
    
    def pop(self):
        if self.top_node is None:
            raise IndexError("Стек пуст")
        value = self.top_node.data
        self.top_node = self.top_node.next
        self.size -= 1
        return value
    
    def peek(self):
        if self.top_node is None:
            raise IndexError("Стек пуст")
        return self.top_node.data
    
    def is_empty(self):
        return self.top_node is None
    
    def __str__(self):
        result = []
        current = self.top_node
        while current is not None:
            result.append(str(current.data))
            current = current.next
        return f"[{', '.join(reversed(result))}]" if result else "[]"


def check_parentheses(expr):
    stack = StackArray()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for ch in expr:
        if ch in pairs:
            stack.push(ch)
        elif ch in pairs.values():
            if stack.is_empty():
                return False
            opening = stack.pop()
            if pairs[opening] != ch:
                return False
    
    return stack.is_empty()
