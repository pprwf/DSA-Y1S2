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
            print("Pop (%s) : " %value, end="")
            self.data.pop()
            self.printStack()
            return value

    def stackTop(self):
        return None if self.data == [] else self.data[-1]

    def printStack(self):
        print(self.data, "\n----------")

# from Lab.Lab03.Stack import ArrayStack


def is_parentheses_matching(expression):
    parsingStack = ArrayStack()
    for i in expression:
        if i == "(":
            parsingStack.push(i)
        elif i == ")":
            parsingStack.pop()
    if parsingStack.data != []:
        print("Parentheses in", expression, "are unmatched")
    return parsingStack.is_empty()

parsingStack = ArrayStack()
str = "(((A - B) * C)"
result = is_parentheses_matching(str)
print(result)
