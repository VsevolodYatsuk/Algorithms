class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            if stack.peek() == bracket_pairs[char]:
                stack.pop()
            else:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    expressions = ["{[()]}", "{[(])}", "{[()]}"]
    for expression in expressions:
        if is_balanced(expression):
            print(f"Строка '{expression}' сбалансирована.")
        else:
            print(f"Строка '{expression}' не сбалансирована.")
