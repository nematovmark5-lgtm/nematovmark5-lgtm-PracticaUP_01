class HashMap:
    class BucketItem:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next_item = None
    
    def __init__(self, initial_size=16):
        self.size = 0
        self.capacity = initial_size
        self.buckets = [None] * initial_size
        self.max_load = 0.75
    
    def _hash_func(self, key):
        h = 0
        for c in str(key):
            h = (h * 31 + ord(c)) % self.capacity
        return h
    
    def _rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0
        
        for item in old_buckets:
            current = item
            while current is not None:
                self.put(current.key, current.value)
                current = current.next_item
    
    def put(self, key, value):
        if self.size / self.capacity >= self.max_load:
            self._rehash()
        
        idx = self._hash_func(key)
        
        if self.buckets[idx] is None:
            self.buckets[idx] = self.BucketItem(key, value)
            self.size += 1
            return
        
        current = self.buckets[idx]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            if current.next_item is None:
                break
            current = current.next_item
        
        current.next_item = self.BucketItem(key, value)
        self.size += 1
    
    def get(self, key):
        idx = self._hash_func(key)
        current = self.buckets[idx]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next_item
        
        raise KeyError(f"Ключ '{key}' отсутствует")
    
    def delete(self, key):
        idx = self._hash_func(key)
        
        if self.buckets[idx] is None:
            raise KeyError(f"Ключ '{key}' отсутствует")
        
        if self.buckets[idx].key == key:
            self.buckets[idx] = self.buckets[idx].next_item
            self.size -= 1
            return
        
        prev = self.buckets[idx]
        current = prev.next_item
        
        while current is not None:
            if current.key == key:
                prev.next_item = current.next_item
                self.size -= 1
                return
            prev = current
            current = current.next_item
        
        raise KeyError(f"Ключ '{key}' отсутствует")
    
    def show(self):
        print(f"Хэш-таблица (элементов: {self.size}, емкость: {self.capacity}):")
        print("-" * 50)
        for i in range(self.capacity):
            print(f"[{i:3}]: ", end="")
            current = self.buckets[i]
            if current is None:
                print("пусто")
            else:
                items = []
                while current is not None:
                    items.append(f"'{current.key}': {current.value}")
                    current = current.next_item
                print(" → ".join(items))
        print("-" * 50)
