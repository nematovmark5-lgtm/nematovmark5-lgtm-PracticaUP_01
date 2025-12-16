class EnhancedTrieNode:
    def __init__(self):
        self.children = {}
        self.is_complete_word = False
        self.prefix_counter = 0
        self.word_counter = 0

class ExtendedTrie:
    def __init__(self):
        self.root = EnhancedTrieNode()
        self.total_words = 0
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = EnhancedTrieNode()
            node = node.children[ch]
            node.prefix_counter += 1
        
        if not node.is_complete_word:
            node.is_complete_word = True
            self.total_words += 1
        node.word_counter += 1
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_complete_word
    
    def prefix_count(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_counter
    
    def autocomplete(self, prefix, limit=10):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        results = []
        self._collect_words(node, prefix, results)
        return sorted(results)[:limit]
    
    def _collect_words(self, node, prefix, results):
        if node.is_complete_word:
            results.append(prefix)
        
        for ch, child in node.children.items():
            self._collect_words(child, prefix + ch, results)
    
    def delete(self, word):
        if not self.search(word):
            return False
        
        path = []
        node = self.root
        
        for ch in word:
            path.append((node, ch))
            node = node.children[ch]
        
        if node.word_counter > 1:
            node.word_counter -= 1
            return True
        
        node.is_complete_word = False
        node.word_counter = 0
        
        for parent_node, ch in reversed(path):
            child_node = parent_node.children[ch]
            child_node.prefix_counter -= 1
            
            if child_node.prefix_counter == 0:
                del parent_node.children[ch]
        
        self.total_words -= 1
        return True
    
    def word_occurrences(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        
        if node.is_complete_word:
            return node.word_counter
        return 0
    
    def all_words(self):
        results = []
        self._collect_words(self.root, "", results)
        return sorted(results)
    
    def statistics(self):
        return {
            'total_words': self.total_words,
            'total_nodes': self._count_nodes(self.root),
            'max_depth': self._max_depth(self.root)
        }
    
    def _count_nodes(self, node):
        if node is None:
            return 0
        
        count = 1
        for child in node.children.values():
            count += self._count_nodes(child)
        return count
    
    def _max_depth(self, node):
        if node is None:
            return 0
        
        max_child = 0
        for child in node.children.values():
            max_child = max(max_child, self._max_depth(child))
        
        return 1 + max_child
