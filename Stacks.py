class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)


# Example usage of the Stack class
if __name__ == "__main__":
    my_stack = Stack()

    print("Is the stack empty?", my_stack.is_empty())

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print("Stack size:", my_stack.size())
    print("Top element:", my_stack.peek())

    popped_item = my_stack.pop()
    print("Popped item:", popped_item)

    print("Is the stack empty?", my_stack.is_empty())
    print("Stack size:", my_stack.size())
