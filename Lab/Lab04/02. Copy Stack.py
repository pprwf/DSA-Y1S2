'''Copy Stack'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def push(self, data):
        print("Push \"%s\" : " %data, end="")
        self.data.append(data)
        self.printStack()

    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
        else:
            value = self.data[-1]
            print("Pop  \"%s\" : " %value, end="")
            self.data.pop()
            self.printStack()
            return value

    def printStack(self):
        print(self.data)

def copyStack(stack1, stack2):
    stack3 = ArrayStack()
    while stack2.data != []:
        print("s2 ", end=""), stack2.pop()
    print("----------")
    while stack1.data != []:
        x = stack1.data[-1]
        print("s1 ", end=""), stack1.pop()
        print("s3 ", end=""), stack3.push(x)
    print("----------")
    while stack3.data != []:
        x = stack3.data[-1]
        print("s3 ", end=""), stack3.pop()
        print("s1 ", end=""), stack1.push(x)
        print("s2 ", end=""), stack2.push(x)
        print("----------")

s1, s2 = ArrayStack(), ArrayStack()
print("----------")
print("s1 ", end=""), s1.push(10), print("s1 ", end=""), s1.push(20)
print("s1 ", end=""), s1.push(30), print("s2 ", end=""), s2.push(15)
print("----------")
copyStack(s2, s1)
print("Stack s1 : ", end=""), s1.printStack()
print("Stack s2 : ", end=""), s2.printStack()
print("----------")
