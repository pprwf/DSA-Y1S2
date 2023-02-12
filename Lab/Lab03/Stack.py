'''Stack'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        print("Size of Stack :", len(self.data))

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
            print("Pop (%s) : " %value, end="")
            self.data.pop()
            self.printStack()
            return value

    def stackTop(self):
        return None if self.data == [] else self.data[-1]

    def printStack(self):
        print(self.data)

dataStack = ArrayStack()
print("----------")
dataStack.push(10)
dataStack.push(20)
dataStack.push(30)
print("Stack : ", end="")
dataStack.printStack()
print("----------")
x = dataStack.pop()
print("x =", x)
dataStack.pop()
print("Stack : ", end="")
dataStack.printStack()
dataStack.pop()
print("----------")
print(dataStack.is_empty())
dataStack.pop()
print("----------")
