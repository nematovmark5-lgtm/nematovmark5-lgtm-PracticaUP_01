import re
import time
from collections import Counter

class WordFrequency:
    def __init__(self):
        self.hash_map = HashMap()
    
    def _process_text(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    
    def build_hash_table(self, text):
        words = self._process_text(text)
        start = time.perf_counter()
        
        for word in words:
            try:
                count = self.hash_map.get(word)
                self.hash_map.put(word, count + 1)
            except KeyError:
                self.hash_map.put(word, 1)
        
        end = time.perf_counter()
        return end - start
    
    def build_counter(self, text):
        words = self._process_text(text)
        start = time.perf_counter()
        counter = Counter(words)
        end = time.perf_counter()
        return dict(counter), end - start
    
    def get_top_n(self, n=10):
        all_items = []
        for bucket in self.hash_map.buckets:
            current = bucket
            while current is not None:
                all_items.append((current.key, current.value))
                current = current.next_item
        
        sorted_items = sorted(all_items, key=lambda x: (-x[1], x[0]))
        return sorted_items[:n]
    
    def analyze(self, text):
        print("Анализ текста:")
        words = self._process_text(text)
        print(f"Всего слов: {len(words)}")
        
        print("\n1. С помощью хэш-таблицы:")
        hash_time = self.build_hash_table(text)
        print(f"Время: {hash_time:.6f} сек")
        
        print("\n2. С помощью Counter:")
        counter_dict, counter_time = self.build_counter(text)
        print(f"Время: {counter_time:.6f} сек")
        
        print(f"\nСравнение:")
        print(f"Counter быстрее в {hash_time/counter_time:.2f} раз")
        
        print("\nТоп-10 частых слов:")
        top_words = self.get_top_n(10)
        for i, (word, freq) in enumerate(top_words, 1):
            print(f"{i:2}. '{word}': {freq}")
