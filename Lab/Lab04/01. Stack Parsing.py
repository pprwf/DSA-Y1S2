'''Stack Parsing'''

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

def is_parentheses_matching(expression):
    parsingStack = ArrayStack()
    print("----------")
    for i in expression:
        if i == "(":
            print("Read ( then ", end="")
            parsingStack.push(i)
        elif i == ")":
            if parsingStack.data == []:
                print("----------\nParentheses in", expression, "are unmatched")
                return False
            print("Read ) then ", end="")
            parsingStack.pop()
    print("----------")
    if parsingStack.data != []:
        print("Parentheses in", expression, "are unmatched")
    return parsingStack.is_empty()

str = "(((A - B) * C)"
result = is_parentheses_matching(str)
print(result)
print("----------")
