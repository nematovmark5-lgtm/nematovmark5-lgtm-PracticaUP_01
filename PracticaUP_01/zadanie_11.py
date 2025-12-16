class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BalancedBST:
    def __init__(self):
        self.root = None
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def insert(self, value):
        self.root = self._insert_node(self.root, value)
    
    def _insert_node(self, node, value):
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert_node(node.left, value)
        elif value > node.value:
            node.right = self._insert_node(node.right, value)
        else:
            return node
        
        self._update_height(node)
        
        balance = self._balance_factor(node)
        
        # Левый-левый случай
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)
        
        # Правый-правый случай
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)
        
        # Левый-правый случай
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Правый-левый случай
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def search(self, value):
        return self._search_node(self.root, value)
    
    def _search_node(self, node, value):
        if node is None or node.value == value:
            return node is not None
        
        if value < node.value:
            return self._search_node(node.left, value)
        return self._search_node(node.right, value)
    
    def delete(self, value):
        self.root = self._delete_node(self.root, value)
    
    def _delete_node(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._min_node(node.right)
            node.value = temp.value
            node.right = self._delete_node(node.right, temp.value)
        
        if node is None:
            return node
        
        self._update_height(node)
        
        balance = self._balance_factor(node)
        
        # Балансировка после удаления
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)
        
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)
        
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)
    
    def preorder(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
    
    def postorder(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, node, result):
        if node is not None:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)
    
    def is_balanced(self):
        return self._check_balance(self.root)
    
    def _check_balance(self, node):
        if node is None:
            return True
        
        balance = abs(self._balance_factor(node))
        
        if balance > 1:
            return False
        
        return self._check_balance(node.left) and self._check_balance(node.right)
