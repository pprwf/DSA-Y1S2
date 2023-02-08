'''Stack'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        print(len(self.data))

    def is_empty(self):
        return True if self.data == [] else False

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
        else:
            value = self.data[-1]
            self.data.pop()
            return value

    def stackTop(self):
        return None if self.data == [] else self.data[-1]

    def printStack(self):
        print(self.data)

dataStack = ArrayStack()
dataStack.push(10)
dataStack.push(20)
dataStack.push(30)
dataStack.printStack()
x = dataStack.pop()
print(x)
dataStack.pop()
dataStack.printStack()
dataStack.pop()
print(dataStack.is_empty())
dataStack.pop()
