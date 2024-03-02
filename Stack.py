class Stack:
    def __init__(self):
        self.items  = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

def reverse_string(input_string):
    stack =  Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
      reversed_string += stack.pop()

    return reversed_string
    

input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {reverse_string}")