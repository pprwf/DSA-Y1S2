'''Stack'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        print("Size of Stack :", len(self.data), "\n----------")

    def is_empty(self):
        print("This stack is empty? : ", end="")
        return self.data == []

    def push(self, data):
        print("Push (%s) : " %data, end="")
        self.data.append(data)
        self.printStack()

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
        print(self.data, "\n----------")

dataStack = ArrayStack()
print("----------")
dataStack.push(10)
dataStack.push(20)
dataStack.push(30)
dataStack.printStack()
x = dataStack.pop()
print(x)
dataStack.pop()
dataStack.printStack()
dataStack.pop()
print(dataStack.is_empty(), "\n----------")
dataStack.pop()
