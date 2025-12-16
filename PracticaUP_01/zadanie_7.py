class ExpressionCalculator:
    def __init__(self):
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
    
    def _is_operator(self, char):
        return char in self.operators
    
    def _get_precedence(self, op):
        return self.operators.get(op, 0)
    
    def _apply_operator(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Деление на ноль запрещено")
            return a / b
        elif op == '^':
            return a ** b
        else:
            raise ValueError(f"Неизвестный оператор: {op}")
    
    def to_rpn(self, expression):
        output = []
        stack = StackArray()
        
        i = 0
        while i < len(expression):
            ch = expression[i]
            
            if ch == ' ':
                i += 1
                continue
            
            if ch.isdigit() or (ch == '-' and (i == 0 or expression[i-1] in '+-*/^(')):
                num = ''
                if ch == '-':
                    num = '-'
                    i += 1
                
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                output.append(num)
                continue
            
            if ch == '(':
                stack.push(ch)
            
            elif ch == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                if not stack.is_empty():
                    stack.pop()
                else:
                    raise ValueError("Несбалансированные скобки")
            
            elif self._is_operator(ch):
                while (not stack.is_empty() and 
                       stack.peek() != '(' and
                       self._get_precedence(stack.peek()) >= self._get_precedence(ch)):
                    output.append(stack.pop())
                stack.push(ch)
            
            i += 1
        
        while not stack.is_empty():
            if stack.peek() == '(':
                raise ValueError("Несбалансированные скобки")
            output.append(stack.pop())
        
        return output
    
    def evaluate_rpn(self, rpn):
        stack = StackArray()
        
        for token in rpn:
            if token.replace('.', '').replace('-', '').isdigit():
                stack.push(float(token))
            elif self._is_operator(token):
                if stack.top_idx < 1:
                    raise ValueError("Недостаточно операндов")
                b = stack.pop()
                a = stack.pop()
                result = self._apply_operator(a, b, token)
                stack.push(result)
            else:
                raise ValueError(f"Неизвестный токен: {token}")
        
        if stack.top_idx != 0:
            raise ValueError("Некорректное выражение")
        
        return stack.pop()
    
    def calculate(self, expression):
        rpn = self.to_rpn(expression)
        return self.evaluate_rpn(rpn)
