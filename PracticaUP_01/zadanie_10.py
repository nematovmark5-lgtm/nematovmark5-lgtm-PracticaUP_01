class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False
        self.freq = 0

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        self.word_stats = {}
    
    def add_word(self, word, frequency=1):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word_end = True
        node.freq += frequency
        
        self.word_stats[word] = self.word_stats.get(word, 0) + frequency
    
    def _collect_all(self, node, prefix, results):
        if node.is_word_end:
            results.append((prefix, node.freq))
        
        for ch, child in node.children.items():
            self._collect_all(child, prefix + ch, results)
    
    def get_completions(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        results = []
        self._collect_all(node, prefix, results)
        
        results.sort(key=lambda x: (-x[1], x[0]))
        return [word for word, _ in results]
    
    def smart_suggestions(self, prefix, limit=5):
        completions = self.get_completions(prefix)
        
        suggestions = []
        for word in completions:
            if word in self.word_stats:
                suggestions.append((word, self.word_stats[word]))
        
        suggestions.sort(key=lambda x: (-x[1], x[0]))
        return suggestions[:limit]
    
    def contains(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word_end
    
    def get_frequency(self, word):
        return self.word_stats.get(word, 0)
