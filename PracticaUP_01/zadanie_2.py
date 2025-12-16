import time

class ArrayDynamic:
    def __init__(self, initial_size=10):
        self.capacity = initial_size
        self.length = 0
        self.storage = [None] * initial_size
    
    def _grow(self):
        new_capacity = self.capacity * 2
        new_storage = [None] * new_capacity
        for i in range(self.length):
            new_storage[i] = self.storage[i]
        self.storage = new_storage
        self.capacity = new_capacity
    
    def append(self, value):
        if self.length >= self.capacity:
            self._grow()
        self.storage[self.length] = value
        self.length += 1
    
    def prepend(self, value):
        if self.length >= self.capacity:
            self._grow()
        for i in range(self.length, 0, -1):
            self.storage[i] = self.storage[i-1]
        self.storage[0] = value
        self.length += 1
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Неверный индекс")
        if self.length >= self.capacity:
            self._grow()
        for i in range(self.length, index, -1):
            self.storage[i] = self.storage[i-1]
        self.storage[index] = value
        self.length += 1
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Неверный индекс")
        for i in range(index, self.length - 1):
            self.storage[i] = self.storage[i+1]
        self.storage[self.length - 1] = None
        self.length -= 1
    
    def find(self, value):
        for i in range(self.length):
            if self.storage[i] == value:
                return i
        return -1
    
    def __str__(self):
        items = []
        for i in range(self.length):
            if self.storage[i] is not None:
                items.append(str(self.storage[i]))
        return f"[{', '.join(items)}]"


def test_performance():
    n = 100000
    
    print("Тест статического массива:")
    start = time.perf_counter()
    fixed = ArrayFixed(n)
    for i in range(n):
        try:
            fixed.add_back(i)
        except BufferError:
            break
    fixed_time = time.perf_counter() - start
    print(f"Время: {fixed_time:.4f} сек")
    print(f"Элементов: {fixed.count}")
    
    print("\nТест динамического массива:")
    start = time.perf_counter()
    dynamic = ArrayDynamic(10)
    for i in range(n):
        dynamic.append(i)
    dynamic_time = time.perf_counter() - start
    print(f"Время: {dynamic_time:.4f} сек")
    print(f"Элементов: {dynamic.length}")
    print(f"Емкость: {dynamic.capacity}")
    
    print(f"\nДинамический быстрее в {fixed_time/dynamic_time:.2f} раз")
